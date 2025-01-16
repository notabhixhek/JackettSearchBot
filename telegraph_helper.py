from telegraph import Telegraph

class TelegraphHelper:
    _instance = None
    __telegraph_token = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(TelegraphHelper, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if self.__telegraph_token is None:
            self.__telegraph_token = self.create_new_telegraph_token("JackettSearchBot")

    def create_new_telegraph_token(self, name):
        tgraph = Telegraph()
        tgraph.create_account(short_name=name)
        return tgraph.get_access_token()

    def get_telegraph_token(self):
        return self.__telegraph_token

    def create_page(self, title, html_content, author_name):
        telegraph = Telegraph(self.get_telegraph_token())
        response = telegraph.create_page(
            title=title,
            html_content=html_content,
            author_name=author_name
        )
        return response