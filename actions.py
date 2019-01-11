from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import send_email
import zomato_app

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		zomatoapp = zomato_app.QueryZomato()
		# Query top 5 restaurants in a sorted order (descending) of the average Zomato user rating (on a scale of 1-5, 5 being the highest). 
		result_json = zomatoapp.search_restaurant(tracker, 5)
		
		# create the response body with resuts from zomato api.
		# The format should be: {restaurant_name} in {restaurant_address} has been rated {rating}.
		response=""
		if result_json['results_found'] == 0:
			response= "no results"
		else:
			response="Showing you top rated restaurants:\n"
			count = 1
			for restaurant in result_json['restaurants']:
				response=response+ str(count) + ". \""
				response=response+ str(restaurant['restaurant']['name']) + "\""
				response=response+ "\n\tin "
				response=response+ str(restaurant['restaurant']['location']['address'])
				response=response+ "\n\thas been rated "
				response=response+ str(restaurant['restaurant']['user_rating']['aggregate_rating'])+ "\n"
				count += 1
		
		dispatcher.utter_message("-----\n"+response)
		return [SlotSet('location', zomatoapp.loc)]

class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		# Query top 10 restaurants in a sorted order (descending) of the average Zomato user rating (on a scale of 1-5, 5 being the highest). 
		zomatoapp = zomato_app.QueryZomato()
		result_json = zomatoapp.search_restaurant(tracker, 10)
		
		# create the email message body with resuts from zomato api. 
		# The mail should have the following details for each restaurant:
		#       Restaurant Name
		#       Restaurant locality address
		#       Average budget for two people
		#       Zomato user rating
		message = "Hi,\n\nAs per your request please find the top rated "+ str(zomatoapp.cuisine)+ " restaurants in "+ str(zomatoapp.loc)+ " below. Enjoy, Bon Appetit!\n\n"
		
		if result_json['results_found'] == 0:
			message=message+ "Sorry, no results found :-("
		else:
			count = 1
			for restaurant in result_json['restaurants']:
				message=message+ str(count) + ". \""
				message=message+ str(restaurant['restaurant']['name']) + "\""
				message=message+ "\n\tAddress: "
				message=message+ str(restaurant['restaurant']['location']['address'])
				message=message+"\n\tRating: "
				message=message+ str(restaurant['restaurant']['user_rating']['aggregate_rating'])
				message=message+ "\n\tAverage price for two: "
				message=message+ str(restaurant['restaurant']['average_cost_for_two'])
				message=message+ str(restaurant['restaurant']['currency'])
				message=message+ "\n"
				count += 1
		message=message+"\n\n\nThanks,\n\tTeam Foodie."
		
		# call the flask email sending utility and send mail
		subject = "Foodie search results of top rated "+ str(zomatoapp.cuisine) + " restaurants in " + str(zomatoapp.loc)
		email_id = tracker.get_slot('emailid').strip(' ')
		recipients = [email_id]
		message = message
		response = send_email.send_mail(recipients, subject, message)
		
		dispatcher.utter_message("-----\n"+response)
		return [SlotSet('emailid', email_id)]