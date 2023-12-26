import requests
from flask import Flask, render_template,request
from io import BytesIO
from PIL import Image
import base64




app = Flask(__name__) #Initialise app

# Config
@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
     city_name = request.form['name']
     url = "https://weatherapi-com.p.rapidapi.com/current.json"
     querystring = {"q":city_name}
     headers = {
			"X-RapidAPI-Key": "b406c0f421msh596ec4a32255210p1d7eebjsn24f733ebe681",
			"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
		}
     response = requests.get(url, headers=headers, params=querystring)
     data=response.json()
     dt=data['location']
     city_name=dt['name']
     region=dt['region']
     country=dt['country']
     map_location=dt['tz_id']
     dt2=data['current']
     temparature_in_cel=dt2['temp_c']
     temparature_in_fr=dt2['temp_f']
     dt3=dt2['condition']
     condition=dt3['text']
     wind=dt2['wind_kph']  
     return render_template('weather.html',temp=temparature_in_cel,weather=condition,condition=condition, country=country,wind=wind,city_name = city_name)
    else:
        return render_template('weather.html')
    


@app.route('/home', methods=['GET', 'POST'])
def light():
   if request.method == 'POST':
    url = "https://rapid-porn.p.rapidapi.com/photo"
    category = request.form['name']
    querystring = {"category": category}
    headers = {
    "X-RapidAPI-Key": "b406c0f421msh596ec4a32255210p1d7eebjsn24f733ebe681",
    "X-RapidAPI-Host": "rapid-porn.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    photo_binary = response.content
    photo_base64 = base64.b64encode(photo_binary).decode('utf-8')
    return render_template('love.html', photo=photo_base64, category=category,)
   else:
      return render_template("love.html")
   
@app.route('/love2',methods=['GET','POST'])
def photo():
   if request.method == 'POST':
      url = "https://rapid-porn.p.rapidapi.com/all-tags"
      headers = {
         "X-RapidAPI-Key": "b406c0f421msh596ec4a32255210p1d7eebjsn24f733ebe681",
         "X-RapidAPI-Host": "rapid-porn.p.rapidapi.com"
         }
      response = requests.get(url, headers=headers)
      if response.status_code == 200:
         tags = response.json()
         tag=tags['tags']
         return render_template('love2.html', tags=tag,)
   else:
      return render_template("love2.html")
    



if __name__ == '__main__':
    app.run(debug=True)