# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from multiprocessing.sharedctypes import Value
from tkinter import Button
from typing import Any, Text, Dict, List
from urllib import response

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Restarted
import pandas as pd
import numpy as np
import requests

#github repository where csv data is located
url = "https://raw.githubusercontent.com/OmdenaAI/hyderabad-india-chapter-patients-chatbot/main/src/data/raw_data/FINAL1.csv?token=GHSAT0AAAAAABT3D53T2INUCPMSSWNCECEMYT7ITMA"
d = requests.get(url).content
#df = pd.read_csv(io.StringIO(d.decode('utf-8')))
df= pd.read_csv(url, encoding='utf-8')

class ActionSymptoms(Action):

     def name(self) -> Text:
         return "action_symptoms"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        disease_slot =  tracker.get_slot('disease')
        obj = disease_identifier()
        disease = obj.disease_track(disease_slot)
        intentAge = tracker.get_slot('age')
        print(f'disease name is {disease}')

        #creating a object for class having the tex_ext function
        obj = text_treatment()

        global df
        
        #checking if the user has provided the name of disease
        if disease is not None:

            df_symp = df[df['condition'] == disease]
            
            #getting symptoms for infants
            if intentAge == "infant":
                
                out = df_symp['Symptoms(babies/infants)'].to_json(orient='records')[1:-1].replace('["', '')
                out = obj.text_ext(out)
                
            #getting symptoms in general
            elif intentAge == "adult":
                
                out = df_symp['Symptoms(common)'].to_json(orient='records')[1:-1].replace('["', '')
                out = obj.text_ext(out)
                print(out)
                #getting symptoms for male
                if df_symp['Symptoms(male)'].isnull().values.all():
                    pass
                else:
                    outM = df_symp['Symptoms(male)'].to_json(orient='records')[1:-1].replace('["', '')
                    outM = obj.text_ext(outM)
                    dispatcher.utter_message("Few symptoms of " + disease + " in Men are: \n")
                    for itemM in outM:
                        dispatcher.utter_message("- " + itemM + "\n")
                    
                    #adding extra line for space
                    dispatcher.utter_message("\n")


                #getting symptoms for female
                if df_symp['Symptoms(female)'].isnull().values.all():
                    pass
                else:
                    outF = df_symp['Symptoms(female)'].to_json(orient='records')[1:-1].replace('["', '')
                    outF = obj.text_ext(outF)
                    
                    dispatcher.utter_message("Few symptoms of " + disease + " in Women are: \n")
                    for itemF in outF:
                        dispatcher.utter_message("- " + itemF + "\n")
                    
                    #adding extra line for space
                    dispatcher.utter_message("\n")

            #getting symptoms for old people
            else:
                out = df_symp['Symptoms(old people)'].to_json(orient='records')[1:-1].replace('["', '')
                out = obj.text_ext(out)

            
            
            if len(out) ==0:
                dispatcher.utter_message("No data avialable")
            else:
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
        #creating a disease identifier object which will identify the disease name from what user types 
        obj = disease_identifier()
        disease = obj.disease_track(disease)
        intentAge = tracker.get_slot('age')
        
        #creating a object for class having the tex_ext function
        obj = text_treatment()

        global df
        
        if disease is not None:

            df_med = df[df['condition'] == disease]
        

            if intentAge == "infant":
                out = df_med['Medication(babies/infants)'].to_json(orient='records')[1:-1].replace('["', '')
                out = obj.text_ext(out)
                
            elif intentAge == "adult":
                out = df_med['Medication(general)'].to_json(orient='records')[1:-1].replace('["', '')
                out = obj.text_ext(out)
                
            else:
                out = df_med['Medication(old people)'].to_json(orient='records')[1:-1].replace('["', '')
                out = obj.text_ext(out)

            
 
            if len(out) ==0:
                dispatcher.utter_message("No data avialable")
            else:
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

        disease_slot =  tracker.get_slot('disease')
        #creating a disease identifier object which will identify the disease name from what user types 
        obj = disease_identifier()
        disease = obj.disease_track(disease_slot)
        intentAge = tracker.get_slot('age')
        
        #creating a object for class having the tex_ext function
        obj = text_treatment()

        global df
        
        if disease is not None:

            df_treat = df[df['condition'] == disease]
        

            if intentAge == "infant":
                out = df_treat['Treatment(babies/infants)'].to_json(orient='records')[1:-1].replace('["', '')
                out = obj.text_ext(out)
                
            elif intentAge == "adult":
                out = df_treat['Treatment(general)'].to_json(orient='records')[1:-1].replace('["', '')
                out = obj.text_ext(out)
                
            else:
                out = df_treat['Treatment(old people)'].to_json(orient='records')[1:-1].replace('["', '')
                out = obj.text_ext(out)

            

            if len(out) ==0:
                dispatcher.utter_message("No data avialable")
            else:
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
        #creating a disease identifier object which will identify the disease name from what user types 
        obj = disease_identifier()
        disease = obj.disease_track(disease)
        intentAge = tracker.get_slot('age')
        
        #creating a object for class having the tex_ext function
        obj = text_treatment()

        global df
        
        if disease is not None:

            df_exp = df[df['condition'] == disease]
        
            out = df_exp['Expenses'].to_json(orient='records')[1:-1].replace('["', '')
            out = obj.text_ext(out) #using the function that cleans and extracts the data from json file
                
            
            if len(out) ==0:
                dispatcher.utter_message("No data avialable")
            else:
                dispatcher.utter_message("Though expenses can vary, here is an estimate: \n")
                for outcome in out:
                    dispatcher.utter_message("- " + outcome + "\n")

        else:
            dispatcher.utter_message("No disease specified. Please specify a disease.")

        return []


class ActionSurvival(Action):
     
     def name(self) -> Text:
         return "action_survival"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        disease =  tracker.get_slot('disease')
        #creating a disease identifier object which will identify the disease name from what user types 
        obj = disease_identifier()
        disease = obj.disease_track(disease)
        
        #creating a object for class having the tex_ext function
        obj = text_treatment()

        global df
        
        if disease is not None:

            df_sur = df[df['condition'] == disease]
        
            out = df_sur['Survival_Rate'].to_json(orient='records')[1:-1].replace('["', '')
            out = obj.text_ext(out) #using the function that cleans and extracts the data from json file
                
            
            if len(out) ==0:
                dispatcher.utter_message("No data avialable")
            else:
                dispatcher.utter_message("Survival rate prediction: \n")
                for outcome in out:
                    dispatcher.utter_message("- " + outcome + "\n")

        else:
            dispatcher.utter_message("No disease specified. Please specify a disease.")

        return []


class ActionPrevent(Action):
     
     def name(self) -> Text:
         return "action_prevent"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        disease =  tracker.get_slot('disease')
        #creating a disease identifier object which will identify the disease name from what user types 
        obj = disease_identifier()
        disease = obj.disease_track(disease)
        
        #creating a object for class having the tex_ext function
        obj = text_treatment()

        global df
        
        if disease is not None:

            df_pre = df[df['condition'] == disease]
        
            out = df_pre['Prevention'].to_json(orient='records')[1:-1].replace('["', '')
            out = obj.text_ext(out) #using the function that cleans and extracts the data from json file
                
            
            if len(out) ==0:
                dispatcher.utter_message("No data avialable")
            else:
                dispatcher.utter_message("Some preventive steps are: \n")
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

        disease_slot =  tracker.get_slot('disease')
        #creating a disease identifier object which will identify the disease name from what user types 
        obj = disease_identifier()
        disease = obj.disease_track(disease_slot)
        
        
        #get globally saved dataframe
        global df
        
        #check for the disease name
        df_faq = df[df['condition'] == disease]

        #filter for only FAQs leaving out the null rows
        df[['FAQ','FAQ Answers']].dropna(axis=0, inplace= True)

        for num in range(len(df_faq)):
            out1 = df_faq['FAQ'].to_json(orient='records')[1:-1].replace('["', '')
            dispatcher.utter_message(out1)
            out2 = df_faq['FAQ Answers'].to_json(orient='records')[1:-1].replace('["', '')
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


class disease_identifier:

    def disease_track(self,disease):
        list_of_diseases = ['covid', 'diabetes', 'diarrhea', 'dengue', 'respiratory', 'heart diseases']
        global count
        global count #to store number of times each character is matched in name of a disease
        global name #store name of disease which has highest amount of character matches
        global num #store the number of counts
        num=0  #initialize with zero
        
        #loop through each disease name in list of diseases
        for item in list_of_diseases:
            #initialize match character count to zero
            count=0
            
            #loop through each character in disease name
            for char in disease:
                
                #check if character is present in item (which is a name of disease from list)
                if char in item:
                    count+=1
            
            #compare the number of character match, retain the name of disease with highest number of chars matched
            if num <= count:
                num = count
                name = item
        print(name)        
        return name


class ActionRestart(Action):

    def name(self) -> Text:
        return "action_restart"

    async def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


             return [Restarted()]