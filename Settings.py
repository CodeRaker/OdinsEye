from ConfigReaders import JsonReader
from Loggers import FileRotationLogger

class SystemSettings:

    def __init__(self):

        # The default settings, will be overrided by vales in the system configuration file
        self.default_settings = {"attempt_heal": True,
                                "check_interval": 1,
                                "logfile_path": "odinseye.log",
                                "logfile_size_in_mb": 10,
                                "logfile_count": 5
        }
        self.system_settings = JsonReader.system_config(system_config, self.default_settings)

        # Configure logging
        self.log = FileRotationLogger(logger_name="OdinsEye", log_level=30, file_path=self.system_settings["logfile_path"], file_size_in_mb=self.system_settings["logfile_size_in_mb"], file_count=self.system_settings["logfile_count"]).get()
        self.log.propagate = False


class TrackerSettings:

    def __init__(self):
        self.tracked_objects = JsonReader.tracker_config(tracker_config)