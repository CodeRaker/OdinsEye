from ConfigReaders import JsonReader
from Loggers import FileRotationLogger

class SystemSettings:

    def __init__(self):
        self.path = "systemconfig.json"
        self.default_settings = {
                                "attempt_heal": True,
                                "check_interval": 1
                                }
        self.system_settings = JsonReader.system_config(self.path, self.default_settings)

class TrackerSettings:

    def __init__(self):
        self.path = "trackerconfig.json"
        self.tracked_objects = JsonReader.tracker_config(self.path)


class RestSettings:

    def __init__(self):
        self.settings = JsonReader.rest_config()


class LogSettings(self):
        self.path = "systemconfig.json"
        self.default_settings = {
                                "log_file_path": "system.log",
                                "log_file_size_in_mb": 10,
                                "log_file_count": 5,
                                "log_system_name": "OdinsEye",
                                "log_level": 30
                                }

        #for setting in self.system_settings:
         #   if setting.startswith("log_"):
          #      exec("self."+setting+" = self.system_settings['"+setting+"']")