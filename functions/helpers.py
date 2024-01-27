def get_threads_from_db(conversation_id):
    from main import db
    doc = db.collection(u'conversations').document(conversation_id).get()

    if doc.exists:
        return doc.to_dict()['threads']
    else:
        return {}


def save_threads_to_db(conversation_id, threads):
    from main import db
    db.collection(u'conversations').document(conversation_id).set({
        u'threads': threads
    })


def init_agency(conversation_id):
    from agency_swarm import Agency

    # # import agents
    # from bitinvest.CEO import CEO
    # from bitinvest.NewsHarvester import NewsHarvester
    # from bitinvest.MarketAnalyzer import MarketAnalyzer

    # # initialize agents
    # ceo = CEO()
    # market_analyzer = MarketAnalyzer()
    # news_harvester = NewsHarvester()

    # # initialize agency - don't forget threads_callbacks
    # agency = Agency([
    #     ceo,
    #     [ceo, market_analyzer],
    #     [ceo, news_harvester],
    #     [market_analyzer, news_harvester]],
    #     shared_instructions='./bitinvest/agency_manifesto.md',
    #     threads_callbacks={
    #         "load": lambda: get_threads_from_db(conversation_id),
    #         "save": lambda threads: save_threads_to_db(conversation_id, threads),
    #     },
    #     async_mode='threading')

    # return agency
