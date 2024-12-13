import requests
import time

def addDatum(seg):
    print("Sending segment:")
    seg['type'] = 'whisper'
    print(seg)
    url = 'http://localhost:5000/addDatum'
    response = requests.post(url, json = seg)

def startRecordingTimestamp():
    ts = time.time() #time since epoch in seconds
    print("Sending start timestamp")
    url = 'http://localhost:5000/startRecordingTimestamp'
    response = requests.post(url, json = {"ts": ts})
