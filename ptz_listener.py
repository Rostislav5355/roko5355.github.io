import firebase_admin
from firebase_admin import credentials, db
import time
import subprocess

cred = credentials.Certificate("firebase/serviceAccount.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ptz-control.firebaseio.com'  # ← Ujisti se, že je to tvoje URL!
})

ref = db.reference('camera/command')
last = None

while True:
    cmd = ref.get()
    if cmd and cmd != last:
        print(f"Received command: {cmd}")
        subprocess.run(['PTZControl.exe', f'/{cmd}'])
        last = cmd
    time.sleep(0.5)
