FROM python:3.7

WORKDIR /credit-app

COPY . .

ADD app.py .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "python", "./app.py" ]
