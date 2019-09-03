import json

class JsonReader:

    """
    The JsonParser class reads a JSON file and converts it to a dictionary object.
    It is instantiated and called by the ClusterController in the __init__ function.
    """
    
    @staticmethod
    def system_config(system_config, default_settings):
        system_settings = default_settings
        try:
            with open(system_config, "r") as config_file:
                data = ""
                for line in config_file:
                    if line.lstrip(" ").startswith("//") or line == "\n":
                        pass
                    else:
                        data += line

            data = json.loads(data)
            system_settings.update(data)

            return system_settings

        except Exception as e:
            raise e

    @staticmethod
    def tracker_config(tracker_config):
        tracker_settings = {}
        try:
            with open(tracker_config, "r") as config_file:
                data = ""
                for line in config_file:
                    if line.lstrip(" ").startswith("//") or line == "\n":
                        pass
                    else:
                        data += line

            tracker_settings = json.loads(data)

            return tracker_settings

        except Exception as e:
            raise e
