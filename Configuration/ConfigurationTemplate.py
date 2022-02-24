class ConfigurationTemplate:
    LOGS_FILE_PATH: str
    LOGS_FILE_NAME: str
    SYSTEM_LOGS_DIR_PATH: str
    LOGS_DIR_PATH: str
    LOGS_DIR_NAME: str

    def __init__(self, configuration: object):
        self.LOGS_FILE_PATH = configuration.LOGS_FILE_PATH
        self.LOGS_FILE_NAME = configuration.LOGS_FILE_NAME
        self.SYSTEM_LOGS_DIR_PATH = configuration.SYSTEM_LOGS_DIR_PATH
        self.LOGS_DIR_PATH = configuration.LOGS_DIR_PATH
        self.LOGS_DIR_NAME = configuration.LOGS_DIR_NAME
        