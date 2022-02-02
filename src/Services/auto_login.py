import requests
import time as t
from datetime import *
import json
import os

iden2 = os.getpid()

json_file = open(f'Services\config.json')
json_file_data = json.load(json_file)
set_hour = json_file_data["Data"]["Auto_login"]["hour"]
set_PM_AM = json_file_data["Data"]["Auto_login"]["PM_AM"]

with open('Services\config.json', "w") as b:
    dic = {"Data": {
        "Api_key": f"{json_file_data['Data']['Api_key']}",
        "Phone_number": f"{json_file_data['Data']['Phone_number']}",
        "ID": f"{json_file_data['Data']['ID']}",
        f"PID": f"{json_file_data['Data']['PID']}",
        "Email": f"{json_file_data['Data']['Email']}",
        "Password": f"{json_file_data['Data']['Password']}",
        "Auto_login": {"PM_AM": f"{json_file_data['Data']['Auto_login']['PM_AM']}",
                       "hour": f"{json_file_data['Data']['Auto_login']['hour']}",
                       "PID2": f"{iden2}"}
    }
    }
    json.dump(dic, b)

def auto_login_script():
    with requests.session() as session:
        for index in range(2):
            print('Logging')
            login_data = {
                "email": f'{json_file_data["Data"]["Email"]}',
                "password": f'{json_file_data["Data"]["Password"]}',
                "loginform": "Login",
            }
            response = session.request("POST", "https://politicsandwar.com/login/", data=login_data)

    t.sleep(3600)
    check_time()


def check_time():
    current_time = datetime.strptime("03/02/21 16:30", "%d/%m/%y %H:%M")
    x = current_time.now()
    current_hour = x.strftime('%I')
    current_PM_AM = x.strftime("%p")

    if current_hour == set_hour and current_PM_AM == set_PM_AM: #Checks if hour and PM/AM/ align with set hour/PM/AM
            print('Logging in')
            auto_login_script()

    elif current_hour > set_hour and current_PM_AM == set_PM_AM: #Checks if current time is bigger than set hour
        print('(2) Logging in')
        auto_login_script()

    else:
        print('Waiting')
        t.sleep(2)
        check_time()


check_time()

