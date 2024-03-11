import requests


def send_smam(requets):
    
    url = "https://smsguru1.p.rapidapi.com/sms"

    payload = {
	    "phone_number": "+917991198925",
	    "text": "Message from SMS Api Guru"
    }
    headers = {
	    "content-type": "application/json",
	    "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	    "X-RapidAPI-Host": "smsguru1.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.json())