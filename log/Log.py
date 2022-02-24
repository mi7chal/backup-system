from datetime import datetime

from Folder import Folder

class Log:

    def __init__(self, datetime: datetime, folders:list[Folder], database: boolean):
        self.datetime = datetime
        self.folders = folders
        self.database = database

    @property
    def datetime(self):
        return self.datetime
    
    @property
    def folders(self):
        return self.folders