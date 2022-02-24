class Folder:
    
    def __init__(self, name: str, files: list[str]):
        self.name = name
        self.files = files
    
    @property
    def name(self):
        return self.name
    
    @property
    def files(self):
        return self.files