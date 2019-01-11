import zomatopy
import json

class QueryZomato():
	def get_cuisine_ids(self):
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85,'american':1,'mexican':73}
		return cuisines_dict

	def get_zomato_user_key(self):
		return {"user_key":"f9001d35fd8e1c230664ef6c1d370ec3"}

	def init_zomatopy(self):
		try:
			self.config = self.get_zomato_user_key()
			self.zomato = zomatopy.initialize_app(self.config)
			return True
		except Exception as e:
			print(str(e))
			return False

	def extract_query_params_from_tracker(self, tracker):
		try:
			self.loc = tracker.get_slot('location')
			self.cuisine = tracker.get_slot('cuisine')
			self.budget = tracker.get_slot('price').strip(' ')
			return True
		except Exception as e:
			print(str(e))
			return False 

	def get_budget_params(self):
		self.mincft = 0
		self.maxcft = 999999 #budget for two more than this amount is insane
		
		if self.budget == 'high':
		    self.mincft = 700
		elif self.budget == 'low':
		    self.maxcft = 299
		elif self.budget == 'mid':
		    self.mincft = 300
		    self.maxcft = 700
		else:
		    return  False
		return True

	def get_latitude_and_longitude_from_zomato(self):
		try:
			location_detail = self.zomato.get_location(self.loc, 1)
			d1 = json.loads(location_detail)
			self.lat = d1["location_suggestions"][0]["latitude"]
			self.lon = d1["location_suggestions"][0]["longitude"]
			return True
		except Exception as e:
			print(str(e))
			return False 

	def get_zomato_cuisine_id(self):
	    cuisines_dict = self.get_cuisine_ids()
	    cuisine_id = str(cuisines_dict.get(self.cuisine.lower()))
	    return cuisine_id

	def get_search_options(self):
	    if self.get_budget_params() == True:
	    	options = {'mincft':self.mincft, 'maxcft':self.maxcft, 'sort':'rating', 'order':'dsc'}
	    else:
	    	options = {'sort':'rating', 'order':'dsc'}
	    return options

	def search_restaurant(self, tracker, limit=5):
		result_json = {'results_found': 0}
		if self.init_zomatopy() == True:
			if self.extract_query_params_from_tracker(tracker) == True:
				if self.get_latitude_and_longitude_from_zomato() == True:
					try:
						options = self.get_search_options()
						cuisine_id = self.get_zomato_cuisine_id()
						results = self.zomato.restaurant_search_with_options("", self.lat, self.lon, cuisine_id, options, limit)
						result_json = json.loads(results)
					except Exception as e:
						print(str(e))
		return result_json




