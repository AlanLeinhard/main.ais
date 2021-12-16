FROM python:3.10-slim-buster
RUN apt update -y && apt upgrade -y
WORKDIR /app
COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . . 
# RUN ./db_create.py
# перенес копи был перед WORKDIR /app
ENV FLASK_APP=app
ENV FLASK_DEBUG=1

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]