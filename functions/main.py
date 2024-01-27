from firebase_admin import initialize_app, credentials
from firebase_functions import https_fn, options
import flask
from firebase_admin import firestore
from helpers import init_agency
from agency_swarm import set_openai_key

cred = credentials.Certificate("./YOUR_SERVICE_ACCOUNT_KEY.json")

initialize_app(cred)
app = flask.Flask(__name__)

db = firestore.client()

db_token = "YOUR_DB_TOKEN" # you can generate it here https://www.random.org/passwords/?num=5&len=32&format=html&rnd=new

set_openai_key("YOUR_OPENAI_KEY")


class Function:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments


class ToolCall:
    def __init__(self, name, arguments):
        self.function = Function(name, arguments)


@app.post("/SendMessage")
def send_message():
    headers = flask.request.headers
    token = headers.get("Authorization").split("Bearer ")[1]
    if token != db_token:
        return flask.Response(status=401, response="Unauthorized")

    conversation_id = headers.get("Openai-Conversation-Id", None)

    agency = init_agency(conversation_id)

    print("data", flask.request.data.decode("utf-8"))

    tool_call = ToolCall("SendMessage", flask.request.data.decode("utf-8"))

    res = agency.main_thread.execute_tool(tool_call)


    return flask.Response(status=200, response=res)


@app.post("/GetResponse")
def get_response():
    headers = flask.request.headers
    token = headers.get("Authorization").split("Bearer ")[1]
    if token != db_token:
        return flask.Response(status=401, response="Unauthorized")

    conversation_id = headers.get("Openai-Conversation-Id", None)

    agency = init_agency(conversation_id)

    tool_call = ToolCall("GetResponse", flask.request.data.decode("utf-8"))

    res = agency.main_thread.execute_tool(tool_call)

    return flask.Response(status=200, response=res)


@https_fn.on_request(memory=options.MemoryOption.MB_512, timeout_sec=180)
def agency(req: https_fn.Request) -> https_fn.Response:
    with app.request_context(req.environ):
        return app.full_dispatch_request()
