import requests
url = 'https://faq-chatbot-training-institute.herokuapp.com/webhooks/rest/webhook' ##change rasablog with your app name
myobj = {
"message": "hi",
"sender": "nick",
}
x = requests.post(url, json = myobj)
print(x.text)