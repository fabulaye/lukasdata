from bs4 import BeautifulSoup

class html_text():
    def __init__(self):
        pass
    

class html_text_builder():
    def __init__(self):
        self.html=html_text()
        
    def get_metadata(self):
        self.html.text
    def build(self,text):
        self.html.text=text
        self.soup=BeautifulSoup(text)
        self.html.links=self.soup.find_all("a",href=True)
        self.html.embeddings=
        self.html.metadata=self.get_metadata()

#how do I get the url