import requests

url = 'http://localhost:5000/addDatum'

def send_output(seg):
    print("Sending segment:")
    print(seg)
    response = requests.post(url, json = seg)
    #print(response.text)
