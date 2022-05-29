FROM rasa/rasa:3.1.0
WORKDIR '/app'
COPY . /app
USER root
# WORKDIR /app
# COPY . /app
COPY ./data /app/data
RUN  rasa train
VOLUME /app
VOLUME /app/data
VOLUME /app/models
CMD ["run","-m","/app/models","--enable-api","--cors","*","--debug" ,"--endpoints", "endpoints.yml", "--log-file", "out.log", "--debug"]
