from flask import Flask, render_template, request, redirect, url_for
import urllib, json

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
	if request.method == 'POST':
		latitude = request.form['lat']
		longitude = request.form['lon']
		
		responseStyle = 'long'; # the length of the response
		citysize = 'cities15000'; # the minimal number of citizens a city must have
		radius = 200; # the radius in KM
		maxRows = 100; # the maximum number of rows to retrieve
		username = 'zippy15';

		url = "http://api.geonames.org/findNearbyPlaceNameJSON?lat=%s&lng=%s&style=%s&cities=%s&radius=%s&maxRows=%s&username=%s" % (latitude,longitude,responseStyle,citysize,radius,maxRows,username)

		response = urllib.urlopen(url)
		r = json.loads(response.read())
		result = r['geonames']
		
		return render_template('output.html', result = result, latitude = latitude, longitude =longitude)
	else:
		return "Some problem occurred."

if __name__=='__main__':
	app.run(debug=True)
