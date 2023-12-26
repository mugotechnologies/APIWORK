import requests

url = "https://love-calculator.p.rapidapi.com/getPercentage"

querystring = {"sname":"Alice","fname":"John"}

headers = {
	"X-RapidAPI-Key": "b406c0f421msh596ec4a32255210p1d7eebjsn24f733ebe681",
	"X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())