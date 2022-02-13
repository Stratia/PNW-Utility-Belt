import tkinter as tk
from tkinter import ttk
import json
from pynotifier import Notification
import subprocess as s
global root

def submit_info(): #Submits info entered in main menu to config.json (Submit Button)
    json_file = open('Services\config.json')
    json_file_data = json.load(json_file)
    email = json_file_data['Data']['Email']
    password = json_file_data['Data']['Password']
    with open('Services\config.json', "w") as b:
        dic = {"Data": {
            "Api_key": f"{api_key.get()}",
            "Phone_number": f"",
            "ID": f"{nation_ID.get()}",
            f"PID": "",
            "Email": f"{email}",
            "Password": f"{password}",
            "Auto_login": {"PM_AM": f"{json_file_data['Data']['Auto_login']['PM_AM']}",
                           "hour": f"{json_file_data['Data']['Auto_login']['hour']}",
                           "PID2": f"{json_file_data['Data']['Auto_login']['PID2']}"}
        }
        }

        json.dump(dic, b)



def kill_process(pid): #Kills all running background scripts (War-Notiyer, Autologin etc)
    json_file = open('Services\config.json')
    json_file_data = json.load(json_file)
    pid = json_file_data["Data"]["PID"]
    pid2 = json_file_data["Data"]["Auto_login"]['PID2']
    s.Popen('taskkill /F /PID {0}'.format(pid), shell=True)
    s.Popen('taskkill /F /PID {0}'.format(pid2), shell=True)

###############################################################

def activate_auto_login(): #Auto login menu
    global nation_password,nation_email
    root.destroy()
    winr = tk.Tk()
    winr.title("Utility Belt")
    winr.geometry('300x380')
    winr.resizable(False, False)
    winr.iconbitmap('Assets\icon.ico')
    winr.eval('tk::PlaceWindow . center')
    winr.tk.call("source", "sun-valley.tcl")
    winr.tk.call("set_theme", "dark")
    l1 = ttk.Label(winr, text='Password')
    l1.pack()

    nation_password = ttk.Entry(winr)
    nation_password.pack()

    l2 = ttk.Label(winr, text='Email')
    l2.pack()

    nation_email = ttk.Entry(winr)
    nation_email.pack()

    try:
        json_file = open('Services\config.json')
        json_file_data = json.load(json_file)
        nation_password.insert(0,f'{json_file_data["Data"]["Password"]}')
        nation_email.insert(0,f'{json_file_data["Data"]["Email"]}')
    except:
        pass

    def submit_cred():
        json_file = open('Services\config.json')
        json_file_data = json.load(json_file)
        try:
            with open('Services\config.json', "w") as b:
                dic = {"Data": {
                    "Api_key": f"{json_file_data['Data']['Api_key']}",
                    "Phone_number": f"{json_file_data['Data']['Phone_number']}",
                    "ID": f"{json_file_data['Data']['ID']}",
                    f"PID": f"{json_file_data['Data']['PID']}",
                    "Email": f"{nation_email.get()}",
                    "Password": f"{nation_password.get()}",
                    "Auto_login": {"PM_AM": f"{user_set_PM_AM.get()}",
                                   "hour": f"{user_set_hour.get()}",
                                   "PID2": f"{json_file_data['Data']['Auto_login']['PID2']}"
                                   }
                }
                }

                json.dump(dic, b)
        except:
            return

    spacer0 = ttk.Label(text='')
    spacer0.pack()

    user_set_PM_AM = ttk.Combobox(winr,values=["PM","AM"])
    user_set_PM_AM.pack()
    user_set_PM_AM.current(1)

    spacer2 = ttk.Label(text='')
    spacer2.pack()

    user_set_hour = ttk.Combobox(winr, values=["01","02","03","04","05","06","07","08"
                                               ,"09","10","11","12"])
    user_set_hour.pack()
    user_set_hour.current(1)
    spacer2 = ttk.Label(text='')
    spacer2.pack()

    submit = ttk.Button(winr, text='Submit Credentials', command=lambda: submit_cred())
    submit.pack()

    spacer2 = ttk.Label(text='')
    spacer2.pack()

    def activate(): #Activates auto_login script
        Notification(
            title='PnW Utility Belt',
            description='Auto login activated',
            # On Windows .ico is required, on Linux - .png
            duration=10,  # Duration in seconds
            urgency='normal'

        ).send()
        s.Popen([r"Services\auto_login.py", ], shell=True)

    act = ttk.Button(winr, text='Activate', command=lambda: activate())
    act.pack()

    spacer3 = ttk.Label(text='')
    spacer3.pack()

    def back():
        winr.destroy()
        app()

    go_back = ttk.Button(winr, text='Back', command=lambda: back())
    go_back.pack()

    tk.mainloop()

###############################################################

def activate_war_notify(): #Triggers activation notification and activates background notify script
    Notification(
        title='PnW Utility Belt',
        description='War Notfiyer activated. Will notify via SMS or popup (Like this one)',
        # On Windows .ico is required, on Linux - .png
        duration=10,  # Duration in seconds
        urgency='normal'

    ).send()
    s.Popen(["Services\war_notifer.py", ], shell=True)


def notify_activate(): #War notify menu
    root.destroy()
    win = tk.Tk()
    win.title("Utility Belt")
    win.geometry('300x340')
    win.resizable(False, False)
    win.iconbitmap('Assets\icon.ico')
    win.eval('tk::PlaceWindow . center')
    win.tk.call("source", "sun-valley.tcl")
    win.tk.call("set_theme", "dark")

    spacer5 = ttk.Label(win, text='Phone Number (Optional)')
    spacer5.pack()

    phone_number_receiver = ttk.Entry(win)
    phone_number_receiver.pack()

    spacer8 = ttk.Label(win, text='Email')
    spacer8.pack()

    email_sender = ttk.Entry(win)
    email_sender.pack()

    spacer9 = ttk.Label(win, text='Email Password')
    spacer9.pack()

    email_sender_password = ttk.Entry(win)
    email_sender_password.pack()

    try:
        json_file = open('Services\config.json')
        json_file_data = json.load(json_file)
        phone_number_receiver.insert(0, json_file_data['Data']['Phone_number'])
        email_sender.insert(0,json_file_data['Data']['Email'])
        email_sender_password.insert(0,json_file_data['Data']['Password'])
    except:
        pass

    spacer9 = ttk.Label(win, text='Note: Email/Password are required to send text \n '
                                  '                 messages from Email\n')
    spacer9.pack()

    wb1 = ttk.Button(win, text='Activate', command=lambda: activate_war_notify())
    wb1.pack()

    def submit_pass_email_cred():
        json_file = open('Services\config.json')
        json_file_data = json.load(json_file)
        with open('Services\config.json', "w") as b:
            dic = {"Data": {
                "Api_key": f"{json_file_data['Data']['Api_key']}",
                "Phone_number": f"{json_file_data['Data']['Phone_number']}",
                "ID": f"{json_file_data['Data']['ID']}",
                f"PID": f"{json_file_data['Data']['PID']}",
                "Email": f"{email_sender.get()}",
                "Password": f"{email_sender_password.get()}",
                "Auto_login": {"PM_AM": f"{json_file_data['Data']['Auto_login']['PM_AM']}",
                               "hour": f"{json_file_data['Data']['Auto_login']['hour']}",
                               "PID2": f"{json_file_data['Data']['Auto_login']['PID2']}"
                               }
            }
            }
            json.dump(dic, b)


    spacer9 = ttk.Label(win, text='')
    spacer9.pack()

    wb3 = ttk.Button(win, text='Submit Credentials',command=lambda:submit_pass_email_cred())
    wb3.pack()

    spacer8 = ttk.Label(win, text='')
    spacer8.pack()

    def back(): #Back to main menu
        win.destroy()
        app()

    wb3 = ttk.Button(win, text='Back', command=lambda: back())
    wb3.pack()

    spacer9 = ttk.Label(win, text='')
    spacer9.pack()

    tk.mainloop()

def app(): #Main Menu
    global root
    root = tk.Tk()
    root.title('Utility Belt')
    root.iconbitmap('Assets\icon.ico')
    root.geometry('300x310')
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')

    root.tk.call("source", "sun-valley.tcl")
    root.tk.call("set_theme", "dark")

    spacer0 = ttk.Label(root, text='API Key')
    spacer0.pack()

    global api_key
    api_key = ttk.Entry(root)
    api_key.pack()

    global nation_ID
    spacer03 = ttk.Label(root, text='Nation ID')
    spacer03.pack()

    nation_ID = ttk.Entry(root)
    nation_ID.pack()

    try:
        json_file = open('Services\config.json')
        json_file_data = json.load(json_file)
        api_key.insert(0, f'{json_file_data["Data"]["Api_key"]}')
        nation_ID.insert(0,f'{json_file_data["Data"]["ID"]}')
    except:
        return

    spacer2 = ttk.Label(root, text='')
    spacer2.pack()

    b1 = ttk.Button(root, text='Submit',command=lambda:submit_info())
    b1.pack()
    spacer3 = ttk.Label(root, text='')
    spacer3.pack()
    b2 = ttk.Button(root, text='War Notifyer',command=lambda:notify_activate())
    b2.pack()

    spacer4 = ttk.Label(root, text='')
    spacer4.pack()

    b3 = ttk.Button(root,text='Auto Login',command=lambda:activate_auto_login())
    b3.pack()
    spacer5 = ttk.Label(root, text='')
    spacer5.pack()
    b4 = ttk.Button(root, text='Kill All Process',command=lambda:kill_process(pid=None))
    b4.pack()

    tk.mainloop()

if __name__ == '__main__':
    app()


