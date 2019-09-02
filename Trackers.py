from Engines import UnixEngine

class CMDStdoutTracker:

    """
    The Tracker class is responsible for monitoring the state of
    entities provided in the config file.
    It is called from and instantiated by the Controller.
    """
    
    def __init__(self):
        self.targets = []
        self.commands = {}
        self.qualifier_of_success = {}
        self.qualifier_of_failure = {}
        self.cmd = UnixEngine()
        self.results = {}

    def check(self):
        for target in self.targets:
            if self.qualifier_of_success[target] in self.cmd.run_command(self.commands[target]):
                self.results[target] = True
            else:
                self.results[target] = False
