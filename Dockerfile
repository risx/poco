FROM python:3.6

RUN pip install boto3 && \
    pip install discord && \
    pip install asyncio

#RUN mkdir /app
COPY . /app
WORKDIR /app

ENTRYPOINT ["python"]
CMD ["discord-bot.py"]

#Exameple build:    docker build . -t sui
#Example run:       docker run sui:latest