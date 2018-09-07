from flask import Flask, render_template, request
from urllib import urlopen
import json

app = Flask(__name__)
key = '1cb40561162db33b4e063549a3ada067'   # api key

@app.route('/', methods=['GET','POST'])
def main():
    if request.method == "POST":
        city = request.form['city']
        url = 'http://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=imperial&APPID=' + key
        response = urlopen(url).read().decode('utf-8')
        obj = json.loads(response)
        weather_id = str(obj["weather"][0]["id"])
        tempf = str(obj["main"]["temp"])
        tempc = round((obj["main"]["temp"] - 32) * 5 / 9,2)
        return render_template('main.html', var_city=city, var_id=weather_id, var_tempf=tempf, var_tempc=tempc)
    if request.method == "GET":
        city = ""
        return render_template('main.html', var_city=city)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
