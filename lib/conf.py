import json

class Conf:
    conf_path = "conf.json"
    json_object = None
    def __init__(self):
        with open(self.conf_path,'r') as f:
            conf_json = f.read()
        self.json_object = json.loads(conf_json)
    def get_endpoint(self):
        return self.json_object['endpoint']
    def get_access_key(self):
        return self.json_object['access_key']
    def get_secret_key(self):
        return self.json_object['secret_key']
    def get_secure(self):
        if self.json_object['secure'] == "true":
            return True
        elif self.json_object['secure'] == "false":
            return False
        else:
            raise Exception("Invalid value:",self.json_object['secure'])