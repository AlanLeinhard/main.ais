FROM python:3.10-slim-buster
RUN apt update -y && apt upgrade -y
# RUN apt install python-dev -y

WORKDIR /app
COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . . 
# RUN ./db_create.py
# перенес копи был перед WORKDIR /app
ENV FLASK_APP=app
ENV FLASK_DEBUG=1
# RUN flask db init
# RUN flask db migrate
# RUN flask db upgrade
# CMD ["python3", "./db_create.py" ]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]