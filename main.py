from instapy import instapy
import yaml
from pathlib import Path


class Website:
    def __init__(self):
        self.username = None
        self.password = None
        self.settings = Path.cwd() / 'Settings.yaml'

    def get_dict(self, website_type: str):
        with open(str(self.settings)) as file:
            settings = yaml.load(file, Loader=yaml.FullLoader)
            website_list = settings.get("Websites")
            website = website_list.get(website_type)

        return website


class Instagram(Website):
    def __init__(self):
        super().__init__()
        settings = self.get_dict("Instagram")
        self.username = settings.get("username")
        self.password = settings.get("password")

    def login(self):
        instapy.InstaPy(username=self.username, password=self.password,).login()


myWebsite = Instagram()
myWebsite.login()
