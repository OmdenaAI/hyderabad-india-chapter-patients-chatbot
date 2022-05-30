## Chatbot Modeling Rasa Framework

To attain the scope of this project to built a chatbot that can help answer questions of admitted patients regarding thier health, [Rasa](https://rasa.com/) was considered as a framework of choice. Rasa is an open source AI conversation tool that utilizes NLP and machine learning to built powerful AI chatbots. It was chosen for it's versatality and for the ease of scalability of the project.

### WorkFlow:

1. Building a conversation flow

At first, a sample conversational flow was decided that can greet and ask few details about a patient to assist them. This became the building block for further addition of responses and custom actions.

 ![ConversationalFlow](https://user-images.githubusercontent.com/89634505/171044324-8943f1ec-56cb-4b6b-a834-550b2b029327.png)

2. Working with Rasa files

There are three main files utilized to cover the architecture of this chatbot, nlu.yml, stories.yml, domain.yml namely. They can be found in data folder [here](https://github.com/OmdenaAI/hyderabad-india-chapter-patients-chatbot/tree/main/src/tasks/task-5-chatbot-modelling-rasa-framework/Chatbot%20Model/data).

Inents contains the examples of user inputs and etities are defined to store information recieved from these inputs. The stored information in slots if further utilized to fetch the data from database and respond accordingly to the users query. For example, name of the disease is collected and stored in slots and that is to used fetch relevant information from the database. 

![intents](https://user-images.githubusercontent.com/89634505/171045169-110a9cec-edce-4ba1-8ddb-73a9f601949a.jpg)

3. Model Deployment

Model is deployed on heroku using socket io and docker container. Few other alternatives were also explored however implementation of socketio and a webpage seemed to be more successful. 

![medibot](https://user-images.githubusercontent.com/89634505/171045415-fceb3c60-9acd-4fc7-b0cf-1508e9e7b141.gif)
