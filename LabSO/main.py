import pyAesCrypt
import os
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


print(os.listdir())

SCOPES = 'https://www.googleapis.com/auth/drive.file'
CLIENT_SECRET = 'client_secret.json'

store = file.Storage('storage.json')
credz = store.get()
if not credz or credz.invalid:
    flow = client.flow_from_clientsecrets(CLIENT_SECRET, SCOPES)
    credz = tools.run_flow(flow, store)

DRIVE = build('drive', 'v3', http=credz.authorize(Http()))


if res:
    MIMETYPE = 'application/pdf'
    data = DRIVE.files().export_media(fileId=res['id'], mimeType=MIMETYPE).execute()
    if data:
        fn= '%s.jpg' % os.path.splitext(filename)[0]
        with open(fn, 'wb') as fh:
            fh.write(data)
        print('Downloaded "%s" (%s)' % (fn, MIMETYPE))
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "foopassword"


# encrypt
#pyAesCrypt.encryptFile(r'photo.jpg', r'‪photo.jpg.aes', password, bufferSize)
# decrypt
#pyAesCrypt.decryptFile('\u202aphoto.jpg.aes', "‪photout.jpg", password, bufferSize)