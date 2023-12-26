import requests

url = "https://send-sms18.p.rapidapi.com/"

payload = {
	"phone_number": "254729812509",
	"text": "value"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "b406c0f421msh596ec4a32255210p1d7eebjsn24f733ebe681",
	"X-RapidAPI-Host": "send-sms18.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())