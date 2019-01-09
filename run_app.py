from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-518392583585-518997643650-518268176528-0b1429d89f0773893e452129ab395f05', #app verification token
							'xoxb-518392583585-518400457713-C1cQ3ZRSScsYecdkwL2Vm0UR', # bot verification token
							'vbW87wlGrOw5YpjSNJ56fOVC', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))