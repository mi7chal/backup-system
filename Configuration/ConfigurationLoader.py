import json


class ConfigurationLoader:

    @staticmethod
    def load_configuration():
        with open("./config.json", "r") as f:
            content = json.loads(f)
            f.close()

        return content
