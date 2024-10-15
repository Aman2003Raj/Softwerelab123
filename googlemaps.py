import googlemaps
from flask import Flask, render_template, request
import os

app = Flask(_name_)

# Replace 'YOUR_API_KEY' with your actual API key from Google Cloud
API_KEY = 'YOUR_API_KEY'
gmaps = googlemaps.Client(key=API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

# Directions API Example
@app.route('/directions')
def get_directions():
    origin = 'VNIT Nagpur'
    destination = 'Nagpur Railway Station'
    directions = gmaps.directions(origin, destination)
    return directions

# Distance Matrix API Example
@app.route('/distance')
def get_distance():
    origin = 'VNIT Nagpur'
    destination = 'Nagpur Railway Station'
    distance = gmaps.distance_matrix(origin, destination)
    return distance

# Geocoding API Example
@app.route('/geocode')
def get_geocode():
    location = 'VNIT Nagpur'
    geocode = gmaps.geocode(location)
    return geocode

# Places API Example
@app.route('/places')
def get_places():
    location = 'VNIT Nagpur'
    places = gmaps.places_nearby(location={'lat': 21.1458, 'lng': 79.0882}, radius=2000)
    return places

if _name_ == '_main_':
    app.run(debug=True)import googlemaps
from flask import Flask, render_template, request
import os

app = Flask(_name_)

# Replace 'YOUR_API_KEY' with your actual API key from Google Cloud
API_KEY = 'YOUR_API_KEY'
gmaps = googlemaps.Client(key=API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

# Directions API Example
@app.route('/directions')
def get_directions():
    origin = 'VNIT Nagpur'
    destination = 'Nagpur Railway Station'
    directions = gmaps.directions(origin, destination)
    return directions

# Distance Matrix API Example
@app.route('/distance')
def get_distance():
    origin = 'VNIT Nagpur'
    destination = 'Nagpur Railway Station'
    distance = gmaps.distance_matrix(origin, destination)
    return distance

# Geocoding API Example
@app.route('/geocode')
def get_geocode():
    location = 'VNIT Nagpur'
    geocode = gmaps.geocode(location)
    return geocode

# Places API Example
@app.route('/places')
def get_places():
    location = 'VNIT Nagpur'
    places = gmaps.places_nearby(location={'lat': 21.1458, 'lng': 79.0882}, radius=2000)
    return places

if _name_ == '_main_':
    app.run(debug=True)