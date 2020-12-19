"""базовая страница - класс-от которой будем наследовать (создавать экземпляры)"""
class BasePage():
    def __init__(self,browser,url):
        self.browser=browser
        self.url=url

    def open(self):
        self.browser.get(self.url)