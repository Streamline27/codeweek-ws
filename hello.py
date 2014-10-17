from flask import render_template
from flask import Flask
import requests
app = Flask(__name__)

@app.route("/")
def hello(name=None):
    return render_template('index.html')

@app.route("/about")
def about():
    return "I am Vlad"

@app.route("/fc")
def forecast():
    API_KEY = "fd6e2be2474579f7314ec9eb4323874d"
    fc_url = "https://api.forecast.io/forecast/{}/56.9496487,24.10518639999998".format(API_KEY)
    #return requests.get(fc_url).text
    
    data = requests.get(fc_url).json()
    hourly_data = data['hourly']['data']
    average = sum([d['temperature'] for d in hourly_data])/len(hourly_data)

    return render_template(
        'forecast.html',
		timezone=data['timezone'],
		c_data=data['hourly']['data'],
		average = average)


if __name__ == "__main__":
    app.run(debug = True)
