import requests
from .services import service
import json

def verify_token(token):
    token_verification_request = requests.post( "http://{}/verify_token".format(service("auth")), headers={"Authorization": "Bearer {}".format(token) } )

    #Obtain the result as JSON
    result = token_verification_request.json()

    #If there was an error, return the error
    if "error" in result:
        return '{ "error": "' + result["error"] + '" }'

    else:
        return json.dumps({'uid': result["uid"]})

