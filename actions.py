from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
import re
import sys

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"f9001d35fd8e1c230664ef6c1d370ec3"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		prices = re.findall(r'\d+', price)
		mincft = 0
		maxcft = sys.maxsize
		if len(prices) == 1:
			if int(prices[0]) >= 700:
			    mincft = 700
			else:
			    maxcft = 299
		else:
			mincft = 300
			maxcft = 700
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85,'american':1,'mexican':73}
		options = {'mincft':mincft, 'maxcft':maxcft, 'sort':'rating', 'order':'dsc'}
		results=zomato.restaurant_search_with_options("", lat, lon, str(cuisines_dict.get(cuisine.lower())), options, 5)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"
		
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]

