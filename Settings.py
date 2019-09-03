from ConfigReaders import JsonReader
from Loggers import FileRotationLogger

class SystemSettings:

    def __init__(self):
        self.read_configuration_files()
        self.configure_logging()

    def read_configuration_files(self):
        # Default settings are overrided by vales in the system configuration file
        self.default_settings = {"attempt_heal": True,
                                "check_interval": 1,
                                "logfile_path": "system.log",
                                "logfile_size_in_mb": 10,
                                "logfile_count": 5,
                                "log_system_name": "OdinsEye",
                                "log_level": 30
        }
        self.system_settings = JsonReader.system_config(system_config, self.default_settings)

    def configure_logging(self):
        self.log = FileRotationLogger(logger_name=self.system_settings["log_system_name"], 
                                        log_level=self.system_settings["log_level"], 
                                        file_path=self.system_settings["logfile_path"], 
                                        file_size_in_mb=self.system_settings["logfile_size_in_mb"], 
                                        file_count=self.system_settings["logfile_count"]).get()
        self.log.propagate = False # If True logging is also printed to stdout


class TrackerSettings:

    def __init__(self):
        self.tracked_objects = JsonReader.tracker_config(tracker_config)