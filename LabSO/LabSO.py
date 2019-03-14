import threading
from time import sleep
import tkinter as tk
from tkinter import filedialog
import os, sys
#import pyAesCrypt
import os
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

def getFolderFiles():
    root = tk.Tk()
    filez = filedialog.askopenfilenames(parent=root,title='Choose a file')
    print(root.tk.splitlist(filez))
    return root.tk.splitlist(filez)

def upload(path):
    FILES = (
        (path, None),
        (path, 'application/vnd.google-apps.document')
    )

    for filename, mimeType in FILES:
        metadata = {'name': filename}
        if mimeType:
            metadata['mimeType'] = mimeType
        res = DRIVE.files().create(body=metadata, media_body=filename).execute()
        if res:
            print('Uploaded "%s" (%s)' % (filename, res['mimeType']))
#Autenticar

SCOPES = 'https://www.googleapis.com/auth/drive.file'
CLIENT_SECRET = 'client_secret.json'

store = file.Storage('storage.json')
credz = store.get()
if not credz or credz.invalid:
    flow = client.flow_from_clientsecrets(CLIENT_SECRET, SCOPES)
    credz = tools.run_flow(flow, store)

DRIVE = build('drive', 'v3', http=credz.authorize(Http()))

print(datatype(getFolderFiles()))
Photos = list(getFolderFiles())
Threads = []

for pic in Photos:
    thread = Thread(target = upload, args = (pic,))
    Threads.add(thread)
    thread.start()
sleep(5)
for thr in Threads:
    thr.join()

sleep(5)
