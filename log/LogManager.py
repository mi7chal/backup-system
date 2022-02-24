import sys
import os
import json
from Configuration import ConfigurationTemplate
import Log


class LogManager:
    configuration: ConfigurationTemplate
    logs: list[Log]
    loaded: bool

    def __init__(self, configuration: ConfigurationTemplate):
        self.configuration = configuration
        self.loaded = False
        self.logs = self.load_logs
        self.loaded = True

    def save_log(self):
        if self.initialised:
            try:
                self.__ready_up_logs_file()

                with open(self.configuration.LOGS_FILE_PATH, "a") as f:
                    content = json.dumps(self.logs)
                    f.write(content)
                    f.close()

            except FileNotFoundError:
                sys.exit(0)
            except:
                self.errorFactory.throw_error("Plik nie moze zostac poprawnie odczytany")
                sys.exit(0)

    def load_logs(self):

        try:
            self.__ready_up_logs_file()

            with open(self.configuration.LOGS_FILE_PATH, "r") as f:
                f = f.readlines()

            for line in f:
                array = line.split(" | ") # TODO obsluga logow
                    self.logs.append(line)
                    break


        except FileNotFoundError:
            sys.exit(0)
        except:
            self.errorFactory.throw_error("Plik nie moze zostac poprawnie odczytany")
            sys.exit(0)

    def __ready_up_logs_file(self):
        if not os.path.isfile(self.configuration.LOGS_FILE_PATH):

            if not os.path.exists(self.configuration.LOGS_DIR_PATH):

                if not os.path.exists(self.configuration.SYSTEM_LOGS_DIR_PATH):
                    self.errorFactory.throwError("Podana sciezka nie istnieje %s"
                                                 % self.configuration.SYSTEM_LOGS_DIR_PATH)
                    raise FileNotFoundError
                else:
                    os.mkdir(self.configuration.LOGS_DIR_PATH)

            with open(self.configuration.LOGS_FILE_PATH, "a") as f:
                f.close()