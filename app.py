'''Mini project-4
Author:Denzil Roy.I
About:A simple weather app which fetches
the live weather forecast of a user specified
region or place.This app uses API(APPLICATION 
PROGRAMMING INTERFACE)to fetch live results.

Features:
1.Can fetch details related to weather of a 
user specified region/country
2.Display the results like wind,Condition,
precipitation etc..'''
from flask import*#importing the flask module
import requests#importing the requests module for api
app=Flask(__name__)#creating an object for the class Flask
API_KEY='738c1cb93c4c4098aa193113242910'
URL='http://api.weatherapi.com/v1/current.json'
@app.route('/')#the route url 
@app.route('/home',methods=['GET','POST'])#home url
def home():
    weather_data=None # a variable which has variable none which would later store the data fetched
    if request.method=='POST':
        location=request.form['location']
        param={ #the parameters passed for the api website to fetch the details
            'q':location,
            'key':API_KEY,
            'units':'metric'
        }
        response=requests.get(URL,params=param)
        if response.status_code==200:
            weather_data=response.json()
        else:
            weather_data={'error':'Region not found'}
        return render_template('weatherpage.html',weather_data=weather_data) #html template to display fetched results to user
    else:
        return render_template('index.html') #html template to get details from user
if __name__=='__main__':
    app.run(debug=True)
