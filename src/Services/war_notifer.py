import requests
import time
from pynotifier import Notification
import json
import os
from twilio.rest import Client

iden = os.getpid()

json_file = open('Services\config.json')
json_file_data = json.load(json_file)
api_key = json_file_data['Data']['Api_key']
nation_id = json_file_data['Data']['ID']
phone = json_file_data["Data"]["Phone_number"]
with open('Services\config.json', "w") as b:
    dic = {"Data": {
        "Api_key": f"{json_file_data['Data']['Api_key']}",
        "Phone_number": f"{json_file_data['Data']['Phone_number']}",
        "ID": f"{json_file_data['Data']['ID']}",
        f"PID": f"{iden}",
        "Email": f"{json_file_data['Data']['Email']}",
        "Password": f"{json_file_data['Data']['Password']}",
        "Auto_login": {"PM_AM": f"{json_file_data['Data']['Auto_login']['PM_AM']}",
                       "hour": f"{json_file_data['Data']['Auto_login']['hour']}",
                       "PID2": f"{json_file_data['Data']['Auto_login']['PID2']}"}
    }
    }
    json.dump(dic, b)


def notification():
    Notification(
        title='War Declaration (PNW)',
        description=f'{trigger_list}',
        duration=5,  # Duration in seconds
        urgency='normal'
    ).send()

    try:
        json_file = open('twillo.json')
        json_file_data2 = json.load(json_file)
        account_sid = f'{json_file_data2["twillo"]["account_sid"]}'
        auth_token = f'{json_file_data2["twillo"]["auth_token"]}'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            messaging_service_sid=f'{json_file_data2["twillo"]["message_service_sid"]}',
            body='War Declaration [PNW Utility Belt]',
            to=f'{json_file_data2["twillo"]["phone_receiver"]}'
        )
    except:
        return


class application:
    def __init__(self):
        call = requests.get(f'https://politicsandwar.com/api/nation/id={nation_id}/&key={api_key}').json()
        #Get Nation ID (input)
        self.cache_war_ids = call['defensivewar_ids']
        self.cache_war_number = call['defensivewars']
        global trigger_list
        trigger_list = [] #Nation ID's that declared new Wars after//Cached ones
        while True:
            time.sleep(120)
            check_call = requests.get(f'http://politicsandwar.com/api/nation/id={nation_id}/&key={api_key}').json()
            if self.cache_war_ids == check_call['defensivewar_ids']:
                pass
            else:
                for index in check_call['defensivewar_ids']:
                    #Checks Individual List Object
                    if index in self.cache_war_ids:
                        pass
                    else:
                        trigger_list.append(index)
                        notification()
                self.cache_war_ids.clear()
                self.cache_war_ids.append(check_call['defensivewar_ids'])

application()
