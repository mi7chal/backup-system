from datetime import datetime


# Tworzy komunikat błędu do zwrócenia w ErrorLogs
class ErrorMessage:

    def __init__(self, message:str, time: datetime):
        self.message = message
        self.datetime = time
    
    # Zwraca komunikat do zapisania w logach
    def get(self):
        return "[% s] [error]: % s \n" % (self.datetime.strftime("%m/%d/%Y, %H:%M:%S"), self.message)
