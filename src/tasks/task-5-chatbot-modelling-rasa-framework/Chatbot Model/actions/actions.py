# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
'''
from tkinter import Button
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_service"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         buttons = [
             {"payload":'/Diabetes{"disease_type":"Diabetes"}', "title":"Diabetes"},

             {"payload":'/FAQS{"disease_type":"Diabetes"',"title":"FAQs"}
         ]
       
         dispatcher.utter_message(f"I could not find universities in", buttons= buttons)

         return []
'''