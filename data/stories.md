## Story 0000000000000000001
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_sendemail
> check_asked_sendemail_question

## user affirms question
> check_asked_sendemail_question
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "someone@somewhere.co.in"}
    - action_send_email
    - slot{"emailid": "someone@somewhere.co.in"}
    - utter_mailsend

## user affirms question
> check_asked_sendemail_question
* get_results_in_mail{"emailid": "someone@somewhere.co.in"}
    - action_send_email
    - slot{"emailid": "someone@somewhere.co.in"}
    - utter_mailsend

## user denies question
> check_asked_sendemail_question
* deny
    - utter_goodbye

## Story 0000000000000000002
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
	- utter_location_limit
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_sendemail
> check_asked_sendemail_question

## Story 0000000000000000003
* greet
    - utter_greet
* restaurant_search{"location": "goa", "cuisine": "north indian"}
    - slot{"location": "goa"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "> 700"}
    - action_restaurant
    - utter_goodbye

## Story 0000000000000000004
* greet
    - utter_greet
* restaurant_search{"location": "italy", "cuisine": "north indian"}
    - slot{"location": "italy"}
	- utter_location_limit
* restaurant_search{"location": "goa", "cuisine": "north indian"}
    - slot{"location": "goa"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "> 700"}
    - action_restaurant
    - utter_ask_sendemail
> check_asked_sendemail_question

##  Story 0000000000000000005
* greet
    - utter_greet
* restaurant_search{"location": "thiruvananthapuram", "cuisine": "mexican", "price": "300-700"}
    - slot{"location": "thiruvananthapuram"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "300-700"}
    - action_restaurant
    - utter_ask_sendemail
> check_asked_sendemail_question

##  Story 0000000000000000006
* greet
    - utter_greet
* restaurant_search{"location": "ooty", "cuisine": "mexican", "price": "mid"}
    - slot{"location": "ooty"}
	- utter_location_limit
* restaurant_search{"location": "thiruvananthapuram", "cuisine": "mexican", "price": "300-700"}
    - slot{"location": "thiruvananthapuram"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "300-700"}
    - action_restaurant
    - utter_ask_sendemail
> check_asked_sendemail_question


##  Story 0000000000000000007
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - action_restaurant
    - utter_ask_sendemail
> check_asked_sendemail_question

##  Story 0000000000000000008
* greet
    - utter_greet
* restaurant_search{"location": "ooty"}
    - slot{"location": "ooty"}
	- utter_location_limit
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - action_restaurant
    - utter_ask_sendemail
> check_asked_sendemail_question

##  Story 0000000000000000009
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - action_restaurant
    - utter_ask_sendemail
> check_asked_sendemail_question

##  Story 0000000000000000010
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh", "cuisine": "chinese"}
    - slot{"location": "rishikesh"}
    - slot{"cuisine": "chinese"}
    - utter_location_limit
* restaurant_search{"location": "delhi", "cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - action_restaurant
    - utter_ask_sendemail
> check_asked_sendemail_question

##  Story 0000000000000000011
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "cuisine": "chinese", "price": "300"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300"}
    - action_restaurant
    - utter_ask_sendemail
> check_asked_sendemail_question

##  Story 0000000000000000012
* greet
    - utter_greet
* restaurant_search{"location": "ooty", "cuisine": "chinese", "price": "300"}
    - slot{"location": "ooty"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300"}
    - utter_location_limit
* restaurant_search{"location": "delhi", "cuisine": "chinese", "price": "300"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300"}
    - action_restaurant
    - utter_ask_sendemail
> check_asked_sendemail_question

## Generated Story 4700931330248361679
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    - export

## Generated Story 8131397312185894717
* greet{"location": "hola"}
    - slot{"location": "hola"}
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - utter_location_limit
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_sendemail
* get_results_in_mail{"emailid": "ahbcdj@dkj.com"}
    - slot{"emailid": "ahbcdj@dkj.com"}
    - action_send_email
    - slot{"emailid": "ahbcdj@dkj.com"}
    - utter_mailsend
    - export

## Generated Story 236254821244267932
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_restaurant
    - slot{"location": "Kolkata"}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "jddk.2jmd@kdl.co.in"}
    - slot{"emailid": "jddk.2jmd@kdl.co.in"}
    - action_send_email
    - slot{"emailid": "jddk.2jmd@kdl.co.in"}
    - utter_mailsend
    - export

## Generated Story -2732441655758330338
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - utter_location_limit
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_restaurant
    - slot{"location": "Mumbai"}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "jddk.2jmd@kdl.co.in"}
    - slot{"emailid": "jddk.2jmd@kdl.co.in"}
    - action_send_email
    - slot{"emailid": "jddk.2jmd@kdl.co.in"}
    - utter_mailsend
    - export

## Generated Story -4744516077768943056
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Chandigarh"}
    - utter_ask_price
* restaurant_search{"price": "<700"}
    - slot{"price": "<700"}
    - action_restaurant
    - slot{"location": "Chandigarh"}
    - utter_ask_sendemail
* deny
    - utter_goodbye
* greet
    - utter_greet
* get_results_in_mail{"emailid": "example@something.com"}
    - slot{"emailid": "example@something.com"}
    - action_send_email
    - slot{"emailid": "example@something.com"}
    - utter_mailsend
    - export

## Generated Story 6243198563120645500
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Chandigarh"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_restaurant
    - slot{"location": "Chandigarh"}
    - utter_ask_sendemail
* deny
    - utter_goodbye
    - export

## Generated Story -1114575028331551319
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Pune", "emailid": "abc.def@gm.co.in"}
    - slot{"cuisine": "chinese"}
    - slot{"emailid": "abc.def@gm.co.in"}
    - slot{"location": "Pune"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_restaurant
    - slot{"location": "Pune"}
    - action_send_email
    - slot{"emailid": "abc.def@gm.co.in"}
    - utter_mailsend
    - export