from flask import*
import requests
app=Flask(__name__)
API_KEY='738c1cb93c4c4098aa193113242910'
URL='http://api.weatherapi.com/v1/current.json'
@app.route('/')
@app.route('/home',methods=['GET','POST'])
def home():
    weather_data=None
    if request.method=='POST':
        location=request.form['location']
        param={
            'q':location,
            'key':API_KEY,
            'units':'metric'
        }
        response=requests.get(URL,params=param)
        if response.status_code==200:
            weather_data=response.json()
        else:
            weather_data={'error':'Region not found'}
        return render_template('weatherpage.html',weather_data=weather_data)
    else:
        return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)