import requests
import time

def addDatum(seg):
    try:
        print("Sending segment:")
        seg['type'] = 'whisper'
        print(seg)
        url = 'http://localhost:5000/addDatum'
        response = requests.post(url, json = seg)
    except:
        print("FAILED: Sending addDatum message")

def startRecordingTimestamp():
    try:
        ts = time.time() #time since epoch in seconds
        print("Sending start timestamp")
        url = 'http://localhost:5000/startRecordingTimestamp'
        response = requests.post(url, json = {"ts": ts})
    except:
        print("FAILED: Sending timestamp message")