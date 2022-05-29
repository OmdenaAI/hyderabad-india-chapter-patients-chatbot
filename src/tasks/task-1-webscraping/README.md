# Task 1: Web Scraping #
The goal of this task was to collect data from various reliable medical pages for the Chatbot and sentiment Analysis. We constricted ourselves to only 6 diseases as of now, following are the disease:
* Covid
* Diabetes
* Respiratory Disease
* Diarrhoeal Disease
* Heart Diseae
* Dengue

Each of these diseases had its own csv filw with 21 columns. The columns are as follows:
* Symptoms(common),
* Symptoms(babies/infants),
* Symptoms(old people)
* Symptoms(male)
* Symptoms(Female)
* Symptoms (critical_stage)
* Medication (general)
* Medication(babies/infants)
* Medication(old people)
* Treatment(general)
* Treatment(babies/infants)
* Treatment(old people)
* Treatment(critical_stage)
* Expenses
* Facts_or_Myths
* Survival_Rate
* Funding
* Prevention
* Diagnosis
* FAQ
* FAQ Answers

After the data collection for chatbot, Patients experience tweets are extracted from twitter using the twitter API. We used multiple keywords and 5 classes to collect the patient experinec tweets. The 5 classes of tweets are listed below:
* Common Procedures (keywords: Surgery, blood etc)
* Emergency Care  (keywords: ICU, NICU, urgent care etc)
* Hospital Staff (keywords: Nurse, doctor, medical rep etc)
* Medical facility (keywords: Hospital, clinic, urgent care etc)
* Treatment (keywords: teat, assist, care etc)

Followed by the tweet collection we perfomed tweet cleaning by removing non english tweets, mentions, urls etc. As most ofthe tweets with URLs turn out to be promotional tweet we discraded  those. After all the cleaning we were left with a total of about 80k tweets.
 

