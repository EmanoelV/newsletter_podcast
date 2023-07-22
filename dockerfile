FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt-get update
RUN Y=y && yes $Y | apt-get install libsndfile1
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]