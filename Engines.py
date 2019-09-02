import subprocess

class UnixEngine:
    """
    The RunScript function of the UnixEngine provides script execution
    capabilities on UNIX-like systems.
    The RunCommand function of the UnixEngine provides command execution
    capabilities on UNIX-like systems. 
    """

    @staticmethod
    def run_script(self):
        pass

    @staticmethod
    def run_command(self):
        try:
            result = subprocess.run(command, shell=True, capture_output=True)
            return result.stdout.decode("utf-8")
        except:
            return False
