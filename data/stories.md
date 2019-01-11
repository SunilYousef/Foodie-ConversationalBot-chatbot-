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