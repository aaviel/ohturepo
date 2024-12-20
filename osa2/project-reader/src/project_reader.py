from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        dict = toml.loads(content)

        name = dict["tool"]["poetry"]["name"]
        description = dict["tool"]["poetry"]["description"]
        license = dict["tool"]["poetry"]["license"]
        authors = dict["tool"]["poetry"]["authors"]
        mainDeps = (dict["tool"]["poetry"]["dependencies"])
        devDeps = (dict["tool"]["poetry"]["group"]["dev"]["dependencies"])

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, mainDeps, devDeps)
