# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from email import message
from multiprocessing.sharedctypes import Value
from tkinter import Button
from typing import Any, Text, Dict, List
from urllib import response

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd
import numpy as np
import csv
import io
import requests

#github repository where csv data is located
url = "https://raw.githubusercontent.com/OmdenaAI/hyderabad-india-chapter-patients-chatbot/main/src/data/raw_data/FINAL1.csv?token=GHSAT0AAAAAABT3D53T2INUCPMSSWNCECEMYT7ITMA"
d = requests.get(url).content
#df = pd.read_csv(io.StringIO(d.decode('utf-8')))
df= pd.read_csv(r"C:/Everything On This PC/Udacity/Chatbot Omdena Hyderabad/FINAL.csv", encoding='utf-8')

class ActionSymptoms(Action):

     def name(self) -> Text:
         return "action_symptoms"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        disease =  tracker.get_slot('disease')
        intentAge = tracker.get_slot('age')

        #creating a object for class having the tex_ext function
        obj = text_treatment()

        global df
        
        #checking if the user has provided the name of disease
        if disease is not None:

            df = df[df['condition'] == disease]

            #getting symptoms for infants
            if intentAge == "infant":
                
                out = df['Symptoms(babies/infants)'].to_json(orient='records')[1:-1].replace('["', '')
                out = obj.text_ext(out)
            
            #getting symptoms in general
            elif intentAge == "adult":
                
                out = df['Symptoms(common)'].to_json(orient='records')[1:-1].replace('["', '')
                out = obj.text_ext(out)
                
                #getting symptoms for male
                if df['Symptoms(male)'].isnull().values.all():
                    pass
                else:
                    outM = df['Symptoms(male)'].to_json(orient='records')[1:-1].replace('["', '')
                    outM = obj.text_ext(outM)
                    dispatcher.utter_message("Few symptoms of " + disease + " in Men are: \n")
                    for itemM in outM:
                        dispatcher.utter_message("- " + itemM + "\n")
                    
                    #adding extra line for space
                    dispatcher.utter_message("\n")


                #getting symptoms for female
                if df['Symptoms(female)'].isnull().values.all():
                    pass
                else:
                    outF = df['Symptoms(female)'].to_json(orient='records')[1:-1].replace('["', '')
                    outF = obj.text_ext(outF)
                    
                    dispatcher.utter_message("Few symptoms of " + disease + " in Women are: \n")
                    for itemF in outF:
                        dispatcher.utter_message("- " + itemF + "\n")
                    
                    #adding extra line for space
                    dispatcher.utter_message("\n")

            #getting symptoms for old people
            else:
                out = df['Symptoms(old people)'].to_json(orient='records')[1:-1].replace('["', '')
                out = obj.text_ext(out)

            #display general symptoms for this age group
            dispatcher.utter_message("Few common symptoms of " + disease + " are: \n")
            
            for item in out:
                dispatcher.utter_message("- " + item + "\n")

        #If the user has not provided the name of the disease it will display following message
        else:
            dispatcher.utter_message("No disease specified. Please specify a disease.")

        return []


class ActionMedication(Action):

     def name(self) -> Text:
         return "action_medication"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        disease =  tracker.get_slot('disease')
        intentAge = tracker.get_slot('age')
        
        #creating a object for class having the tex_ext function
        obj = text_treatment()

        global df
        
        if disease is not None:

            df = df[df['condition'] == disease]
        

            if intentAge == "infant":
                out = df['Medication(babies/infants)'].to_json(orient='records')[1:-1].replace('["', '')
                out = obj.text_ext(out)
                
            elif intentAge == "adult":
                out = df['Medication(general)'].to_json(orient='records')[1:-1].replace('["', '')
                out = obj.text_ext(out)
                
            else:
                out = df['Medication(old people)'].to_json(orient='records')[1:-1].replace('["', '')
                out = obj.text_ext(out)

            dispatcher.utter_message("Some medication for " + disease + " are: \n")

            for item in out:    
                dispatcher.utter_message("- " + item + "\n")

        else:
            dispatcher.utter_message("No disease specified. Please specify a disease.")


        return []


class ActionTreatment(Action):

     def name(self) -> Text:
         return "action_treatment"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        disease =  tracker.get_slot('disease')
        intentAge = tracker.get_slot('age')
        
        #creating a object for class having the tex_ext function
        obj = text_treatment()

        global df
        
        if disease is not None:

            df = df[df['condition'] == disease]
        

            if intentAge == "infant":
                out = df['Treatment(babies/infants)'].to_json(orient='records')[1:-1].replace('["', '')
                out = obj.text_ext(out)
                
            elif intentAge == "adult":
                out = df['Treatment(general)'].to_json(orient='records')[1:-1].replace('["', '')
                out = obj.text_ext(out)
                
            else:
                out = df['Treatment(old people)'].to_json(orient='records')[1:-1].replace('["', '')
                out = obj.text_ext(out)

            dispatcher.utter_message("Some treatments for " + disease + " are: \n")

            for item in out:    
                dispatcher.utter_message("- " + item + "\n")

        else:
            dispatcher.utter_message("No disease specified. Please specify a disease.")


        return []


class ActionExpense(Action):
     
     def name(self) -> Text:
         return "action_expense"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        disease =  tracker.get_slot('disease')
        intentAge = tracker.get_slot('age')
        
        #creating a object for class having the tex_ext function
        obj = text_treatment()

        global df
        
        if disease is not None:

            df = df[df['condition'] == disease]
        
            if intentAge == "infant":
                out = df['Expenses'].to_json(orient='records')[1:-1].replace('["', '')
                out = obj.text_ext(out) #using the function that cleans and extracts the data from json file
                
            elif intentAge == "adult":
                out = df['Expenses'].to_json(orient='records')[1:-1].replace('["', '')
                out = obj.text_ext(out)
                
            else:
                out = df['Expenses'].to_json(orient='records')[1:-1].replace('["', '')
                out = obj.text_ext(out)

            dispatcher.utter_message("Though expenses can vary, here is an estimate: \n")

            for outcome in out:
                dispatcher.utter_message("- " + outcome + "\n")

        else:
            dispatcher.utter_message("No disease specified. Please specify a disease.")

        return []

     
class ActionAnwserFAQ(Action):

     def name(self) -> Text:
         return "action_answer_FAQ"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        med = tracker.get_slot('medication')
        disease =  tracker.get_slot('disease')
        intentAge = tracker.get_slot('age')
        
        #get globally saved dataframe
        global df
        
        #check for the disease name
        df = df[df['condition'] == disease]

        #filter for only FAQs leaving out the null rows
        df[['FAQ','FAQ Answers']].dropna(axis=0, inplace= True)

        for num in range(len(df)):
            out1 = df['FAQ'].to_json(orient='records')[1:-1].replace('["', '')
            dispatcher.utter_message(out1)
            out2 = df['FAQ Answers'].to_json(orient='records')[1:-1].replace('["', '')
            dispatcher.utter_message(out2)
            
        return []


class text_treatment:

    def text_ext(self,text):
            #empty list to collect the indexes where " (double inverted commas) occur
            listIdx = []
            #empty list to collect the output
            final = []
            
            text = text.replace("null",'')
            #collecting the indexes of "
            for index in range(len(text)):
                if text[index] =="\"":
                    listIdx.append(index)
                else:
                    pass
            
            for idx in range(len(listIdx)):
                #collect the data by index starting with 
                if idx%2!=0:
                    final.append(text[listIdx[idx-1]+1:listIdx[idx]])

            return final