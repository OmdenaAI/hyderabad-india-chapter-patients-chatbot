## Deployment Tools Explored ##

 ### ngrok ###
*   ngrok is a cross-platform application that exposes local server ports to the Internet.
*   Easy to use, fast, supports UTP and HTTPS, free.
 ### Heroku with Docker ###
*   Heroku is a container-based cloud Platform as a Service (PaaS).
*   Docker is an open source containerization platform. It enables developers to package applications into deployable units called containers. 
*   Heroku provides two ways for you to deploy your app with Docker:
    *   Container Registry allows you to deploy pre-built Docker images to Heroku.
    *   Build your Docker images with heroku.yml for deployment to Heroku.

## Deployment steps using ngrok on Telegram Channel ##
*  Install ngrok on your system.
*  Add the following to your credintials.yml file :
   *  Add the ***access_token*** and ***verify*** tokens from the telegram channel for the bot.
   *  Start the ngrok CLI with the command - *ngrok http 5005*** - and add the generated ***Forwarding*** token from CLI to the ***webhook_url*** placeholder in credentials.yml file.
   

## Deployment steps using Heroku and Docker  on Telegram Channel ##
*  Install docker and docker-compose on your system.
*  Copy the Dockerfile and docker-compose.yml file in the root directory.
*  Copy the Dockerfile_actions in the actions directory and rename it to "Dockerfile".
*  Put requirements.txt file in the actions dierctory, containing python libraries that you installed and used in the actions.py script. 
*  In the endpoints.yml file,change the name localhost to action_server : <br />
   &nbsp;&nbsp;&nbsp;&nbsp;***action_endpoint:***<br />
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***url: "http://action_server:5055/webhook"***
*  Run the following command to generate the docker-compose image :<br />
   &nbsp;&nbsp;&nbsp;&nbsp;        ***Docker-compose up --build***
*  Create a Heroku account and follow the below commands to push the docker image to heroku and generate a heroku url :
   *   ***heroku container:login***
   *   ***heroku container:push web –recursive***
   *   ***heroku container:release web***

*  Place the above generated heroku url in the ***webhook_url*** placeholder of credentials.yml file.
*  Add the ***access_token*** and ***verify*** tokens from the telegram channel for the bot.

For more information on using docker with rasa, you can refer the following [rasa documentation](https://rasa.com/docs/rasa/docker/building-in-docker/) page.

    


