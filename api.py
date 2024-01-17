# api.py
import os

def hae_saa_api_avain():
    saa_api_avain = os.environ.get('7ea927d6-b511-11ee-84d9-0242ac130002-7ea92858-b511-11ee-84d9-0242ac130002')
    if not saa_api_avain:
        print("Sää-API-avainta ei ole asetettu. Ohjelma saattaa toimia rajoitetusti.")
    return saa_api_avain
