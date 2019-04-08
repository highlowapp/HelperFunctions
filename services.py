from .read_json_from_file import *

def service(service):
    service_config = read_json_from_file("config/services.json")
    return service_config[service]


    