import xml.etree.ElementTree as ET
import os
import sys
from pathlib import Path
from ftplib import FTP
import socket,struct



def parse_xmlfile(filepath):
    file_descriptor = open(filepath,"r")
    a = parse_xml(file_descriptor)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket Created")
    port = a['Port']
    host = a['Host']
    ip = socket.gethostbyname(host)

    # print (ip)
    print ("ip of " +host+ " is " +ip)
    s.connect ((ip, int(port)))
    print ("Socket Connected to "+host+" on ip "+ ip)




def parse_xml(f):
    root = ET.parse(f).getroot()
    data = root.findall('FTP-Account')
    context = {}
    for i in data:
        Host = i.find('Hostname')
        if not Host is None:context['Host'] = Host.text

        Port = i.find('Port')
        if not Port is None:context['Port'] = Port.text

        Username = i.find('Username')
        if not Username is None:context['Username'] = Username.text

        Password = i.find('Password')
        if not Password is None:context['Password'] = Password.text

        Sync_Direction = i.find('Sync-Direction')
        if not Sync_Direction is None:context['Sync-Direction'] = Sync_Direction.text

        Sync_Directory = i.find('Sync-Directory')
        if not Sync_Directory is None:context['Sync-Directory'] = Sync_Directory.text

        Email_Notify = i.find('Email-Notify')
        if not Email_Notify is None:context['Email-Notify'] = Email_Notify.text

    return context

      


if __name__ == '__main__':
    try:
        arg = sys.argv[1]
        if not os.path.isfile(arg):
            print("file not found")        
        else:
            parse_xmlfile(arg)
    except Exception as e:
        print("usage: python3 main.py file_path")