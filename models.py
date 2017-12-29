from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
from flask import Flask
#For nearby places, libs  below
import geocoder
import urllib3
import json

db = SQLAlchemy() 

class User(db.Model):
    __tablename__='Users'
    Name = db.Column(db.String(100), primary_key=True)
    Email = db.Column(db.String(100))
    Address = db.Column(db.String(100))

    def __init__(self, name, email, address):
        self.Name = name.title()
        self.Email = email.title()
        self.Address = address.title()

# p = Place()
# places = p.query("1600 Amphitheater Parkway Mountain View CA")
class Place(object):
  def meters_to_walking_time(self, meters):
    # 80 meters is one minute walking time
    return int(meters / 80)  

  def wiki_path(self, slug):
    return urllib3.urlparse.urljoin("http://en.wikipedia.org/wiki/", slug.replace(' ', '_'))
  
  def address_to_latlng(self, address):
    g = geocoder.google(address)
    return (g.lat, g.lng)

  def query(self, address):
    lat, lng = self.address_to_latlng(address)
    http = urllib3.PoolManager()
    query_url = 'https://en.wikipedia.org/w/api.php?action=query&list=geosearch&gsradius=5000&gscoord={0}%7C{1}&gslimit=20&format=json'.format(lat, lng)
    g = http.request('GET', query_url)
    results = g.read()
    g.close()

    data = json.loads(results)
    
    places = []
    for place in data['query']['geosearch']:
      name = place['title']
      meters = place['dist']
      lat = place['lat']
      lng = place['lon']

      wiki_url = self.wiki_path(name)
      walking_time = self.meters_to_walking_time(meters)

      d = {
        'name': name,
        'url': wiki_url,
        'time': walking_time,
        'lat': lat,
        'lng': lng
      }

      places.append(d)

    return places
