# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import pandas as pd
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):

# 	def name(self) -> Text:
# 		return "action_hello_world"

# 	def run(self, dispatcher: CollectingDispatcher,
# 			tracker: Tracker,
# 			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

# 		button = [{
# 					  "title": "Babies/Infants",
# 					  "payload": "Babies/Infants"
# 				  },
# 				  {
# 					  "title": "General",
# 					  "payload": "General"
# 				  }]

# 		dispatcher.utter_message(text="Choose one of the buttons:",buttons = button)
# 		#dispatcher.utter_button_message(message, buttons)

# 		return []

class ActionInfo(Action):

	def name(self) -> Text:
		return "action_read_info"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		#t = tracker.latest_message['text']
		disease = tracker.slots.get('disease_condition')
		disease = disease.lower()
		if disease not in ['dengue','diabetes','diarrhea','covid','heart disease','respiratory infection']:
			dispatcher.utter_message(text="Sorry! I don't have information about this disease yet. I will try to learn about it and help you in the future.")
			return []
		if disease=='heart disease':
			disease = "heart_disease"
		if disease=='respiratory infection':
			disease = "respiratory_infection"
		file_name = "F:\\rasa_chatbot_project\\disease_files\\"+disease+".csv"
		df = pd.read_csv(file_name,engine = 'python',encoding="latin-1")
		c=0
		t=""
		for event in tracker.events[::-1]:
			if event.get("event") == "user":
				c+=1
				if c==2:
					t = event.get("text")
					break

		age_group = ""
		s = tracker.latest_message['intent']['name']
		if s=="babies_infants":
			age_group = "babies/infants"
		elif s=="old_people":
			age_group = "old people"
		elif s=='critical_stage':
			age_group = "critical_stage"
		elif s=='male':
			age_group = "male"
		elif s=='female':
			age_group = "female"
		elif s=='faq':
			if "FAQ" in df.columns:
				data = ""
				for q,a in zip(df['FAQ'],df['FAQ Answers']):
					data += q
					data +='\n'
					data += a
					data +='\n\n'
			else:
				data = "Sorry! I don't have any FAQs for "+disease+" currently. I will try to learn about them and help you in the future."
			dispatcher.utter_message(text=data)
			return []
		else:
			age_group = "common"


		if "symptoms" in t.lower():
			t= "Symptoms"
			t+='('+age_group+')'
			if t in df.columns:
				data = df[t]
			else:
				data = "Sorry! I don't have this information for "+disease+" currently. I will try to learn it and help you in the future."
		elif "prevention" in t.lower():
			t= "Prevention"
			if t in df.columns:
				data = df[t]
			else:
				data = "Sorry! I don't have this information for "+disease+" currently. I will try to learn it and help you in the future."
		elif ("facts"  in t.lower()) or ("myths"  in t.lower()):
			t = "Facts_or_Myths"
			if t in df.columns:
				data = df[t]
			else:
				data = "Sorry! I don't have this information for "+disease+" currently. I will try to learn it and help you in the future."
		elif "fund" in t.lower():
			t = 'Funding'
			if t in df.columns:
				data = df[t]
			else:
				data = "Sorry! I don't have this information for "+disease+" currently. I will try to learn it and help you in the future."
		elif "diagnosis" in t.lower():
			t = 'Diagnosis'
			if t in df.columns:
				data = df[t]
			else:
				data = "Sorry! I don't have this information for "+disease+" currently. I will try to learn it and help you in the future."
		elif ("medication" in t.lower()) or ("medicine" in t.lower()):
			t = 'Medication'
			if age_group=='common':
				age_group = 'general'
			t+='('+age_group+')'
			if t in df.columns:
				data = df[t]
			else:
				data = "Sorry! I don't have this information for "+disease+" currently. I will try to learn it and help you in the future."
		elif ("treatment" in t.lower()):
			t = 'Treatment'
			if age_group=='common':
				age_group = 'general'
			t+='('+age_group+')'
			if t in df.columns:
				data = df[t]
			else:
				data = "Sorry! I don't have this information for "+disease+" currently. I will try to learn it and help you in the future."
		elif ("expense" in t.lower()) or ("cost" in t.lower()) or ("price" in t.lower()):
			t = "Expenses"
			if t in df.columns:
				data = df[t]
			else:
				data = "Sorry! I don't have this information for "+disease+" currently. I will try to learn it and help you in the future."
		elif ("survival" in t.lower()):
			t = "Survival_Rate"
			if t in df.columns:
				data = df[t]
			else:
				data = "Sorry! I don't have this information for "+disease+" currently. I will try to learn it and help you in the future."
		else:
			if "FAQ" in df.columns:
				data = ""
				for q,a in zip(df['FAQ'],df['FAQ Answers']):
					data += "Question : "+q
					data +='\n'
					data += "Answer : "+a
					data +='\n\n'
			else:
				data = "Sorry! I don't have any FAQs for "+disease+" currently. I will try to learn about them and help you in the future."
			dispatcher.utter_message(text=data)
			return []

		data = data.dropna()
		if len(data)==0:
			data = "Sorry! I don't have this information for "+disease+" currently. I will try to learn it and help you in the future."
			dispatcher.utter_message(text=data)
			return []
		
		dispatcher.utter_message(text=data.to_string(index=False))
		return []
