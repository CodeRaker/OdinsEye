import sys
import multiprocessing
import threading

from Trackers import CMDStdoutTracker
from Medics import UnixMedic
from Servers import RESTServer
from Settings import SystemSettings, TrackerSettings, LogSettings

from Multitask import MProcessPipe

class LogController()
    def configure_logging(self):
    self.log = FileRotationLogger(logger_name=self.system_settings["log_system_name"], 
                                    log_level=self.system_settings["log_level"], 
                                    file_path=self.system_settings["log_file_path"], 
                                    file_size_in_mb=self.system_settings["log_file_size_in_mb"], 
                                    file_count=self.system_settings["log_file_count"]).get()
    self.log.propagate = False # If True logging is also printed to stdout

class MainController(SystemSettings, TrackerSettings):

    """
    The MainController handles the OdinsEye components. It is the core code and where the main logic takes place. 
    Below is a list of what the controller does.
    -----------------------------------------------------------------------------------------------------------------
    1. Instantiates and calls the tracker object, to health check entities configured in config.json
    2. Instantiates and calls the medic object, that attempts to heal failing entities configured in config.json

    """


    # read config file
    # configure components from config file settings
    # spawn webserver in its own process, give it a pipe
    # spawn a tracker process that runs all monitoring, give it a pipe
    # spawn a medic process that runs all attempted heals, give it a pipe
    # the idea with all the processes, is to keep the main process free to loop through and not wait for webserver,
    # medic, tracker. The main process makes decisions and delegates tasks to subprocesses.
    # Later it would be interesting to add some decision logic.

    def __init__(self):

        # Instantiate singleton classes, to be controlled later
        self.cmd_stdout_tracker = CMDStdoutTracker()
        self.unix_medic = UnixMedic()
        self.rest_server = RESTServer()

    #def start_odin_service(self, ):



    def start_rest_api(self):
        self.rest_api_process, self.rest_api_pipe = MProcessPipe.spawn(self.rest_server)



    def run_checks(self):
        self.tracker.check()
        recheck = False
        failed = False

        for key in self.tracker.results:

            # If a check has failed, check if heal is enabled
            if not self.tracker.results[key]:
                failed = True
                self.log.warning("Tracker identified a failed check for "+str(key))
                if key in self.medic.patients:
                    self.log.warning("Attempting to heal "+key)
                    self.medic.heal(key)
                    recheck = True

        # No errors found
        if not failed and not recheck:
            sys.exit(0)

        # Recheck happens if a heal has been attempted
        if recheck:
            self.tracker.check()
            failed = False

            # Recheck the results
            for key in self.tracker.results:
                if not self.tracker.results[key]:
                    self.log.error("Heal did not work")
                    sys.exit(1)
            self.log.info("Heal did work!")
            sys.exit(0)

        else:
            if failed:
                sys.exit(1)
            else:
                sys.exit(0)
