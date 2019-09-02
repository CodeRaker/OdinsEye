from Engines import UnixEngine

class UnixMedic:

    """
    The medic is a class representing methods of repairing
    monitored entities in the cluster. The medic relies on
    scripts and commands to heal the cluster.
    """
    
    def __init__(self):
        self.patients = []
        self.treatments = {}
        self.cmd = UnixEngine()

    def heal(self, patient):
        self.cmd.run_command(self.treatments[patient])
