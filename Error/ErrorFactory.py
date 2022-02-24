import os
from datetime import datetime

from ErrorMessage import ErrorMessage


ERROR_FILE_NAME = "error_logs.txt"


# Obsluguje bledy
class ErrorFactory:
    
    def __init__(self, logsPath: str, logsDirPath: str):
        self.SYSTEM_LOGS_DIR_PATH = logsPath
        self.LOGS_DIR_PATH = logsDirPath

    # Zapisuje blad do pliku 
    def throw_error(self, message: str):
        error_message = ErrorMessage(message, datetime.now())
        if not os.path.exists(self.SYSTEM_LOGS_DIR_PATH):
            path = os.path.join(os.getcwd(), ERROR_FILE_NAME)
            with open(path, "a") as f:
                f.write(error_message.get())
                f.close()
        else:
            if not os.path.exsists(self.LOGS_DIR_PATH):
                os.mkdir(self.LOGS_DIR_PATH)
            
            path = os.path(self.LOGS_DIR_PATH, ERROR_FILE_NAME)
            with open (path, "a") as f:
                f.write(error_message.get())
                f.close()
