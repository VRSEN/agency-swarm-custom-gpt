# Agency Swarm Custom GPT Integration


Welcome to the Agency Swarm Custom GPT Integration! This project is designed to integrate multi-agent frameworks into Custom GPTs, making them accessible and usable in the real world, regardless of technical expertise.

# Getting Started
## Prerequisites
* Firebase account
* OpenAI API key
* Firebase Tools (if not already installed)

## Setup Instructions
1. **Create a project on [Firebase](https://firebase.google.com/).**
2. **Enable billing and firestore on your project**.
3. **Create a service account key and drop it into `functions` directory.**
4. **Add path to your service account key in the `main.py` file.**
5. **Add your keys**:  
   Add your openai key in `main.py`. Then, generate a db token using [this link](https://www.random.org/passwords/?num=5&len=32&format=html&rnd=new) and paste it into the `db_token` variable in the `main.py` file.
6. **Replace your project id in the `.firebaserc` file.**
7. **Navigate to the functions directory**:
    ```bash
    cd functions
    ```
8. **Activate the virtual environment**:
    ```bash
    # macOS
    python3 -m venv venv
    source venv/bin/activate
   
    # Windows
    py -m venv venv
    venv\Scripts\activate
9. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

10. **Add your Agency**:  
   Copy all your agents into the functions directory and import them according to an example in the `helpers.py` `init_agency` method. Alternatively, you can create your agency directly in `helpers.py` if it's simple.

12. **Create settings and schema schema**:  
    ```bash
    python schema.py
    ```
13. **Install firebase CLI**:
    ```bash
    npm install -g firebase-tools
    ```

14. **Login to firebase**:
    ```bash
    firebase login
    ```
15. **Deploy**:
    ```bash
    firebase deploy --only functions
    ```
16. **Replace server url**:  
Copy your function url from the terminal and paste it into the `schema.py` file. Run this file locally again with `python schema.py` to update the schema.

17. **Setup Custom GPT**:  
    Copy your CEO agent name, instructions and description into Custom GPT. Create an action with the schema from `schema.json`. Add Bearer authentication with your `db_token` from `main.py` and you're good to go!

# Discord Community
Join our Discord server to be part of a growing community that shapes the future of AI. Share your work, get help, and collaborate with fellow enthusiasts.

Discord Invite Link

# Subscribe and Stay Updated
Don't forget to subscribe to our YouTube channel for the latest updates, tutorials, and discussions on AI and AGI.

[YouTube Channel Link](https://youtube.com/@vrsen?si=CsHkLay_ulWlzJVd)


