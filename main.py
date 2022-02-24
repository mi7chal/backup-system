import sys

from Error.ErrorFactory import ErrorFactory

LOGS_FILE_PATH = "/var/logs/KopiaZapasowa/logs.json"
LOGS_FILE_NAME = "logs.json"
SYSTEM_LOGS_DIR_PATH = "/var/logs/"
LOGS_DIR_PATH = "/var/logs/KopiaZapasowa/"
LOGS_DIR_NAME = "KopiaZapasowa"


class Main:

    def __init__(self):
        self.initialised = False
        self.logs = None
        self.errorFactory = ErrorFactory(SYSTEM_LOGS_DIR_PATH, LOGS_DIR_PATH)

    def initialise(self):
        self.load_logs()
        if not self.check_system():
            self.errorFactory.throwError("nieobslugiwany system ;c")
            sys.exit(0)
        
        self.initialised = True

    def run_backup(self):
        pass
        

    def backup_database(self):
        pass

    def backup_location(self):
        pass



    @staticmethod
    def __check_system():
        if sys.platform == "linux" or sys.platform == "linux2":
            return True
        elif sys.platform == "darwin":
            return True
        else:
            return False


main = Main()
main.initialise()