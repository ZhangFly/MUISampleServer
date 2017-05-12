FROM python:2.7

RUN pip install importlib
RUN pip install demjson
RUN pip install web.py
RUN pip install PyWavelets
RUN pip install pyYaml
RUN pip install SciPy

ADD /src /code
RUN mkdir /code/log
WORKDIR /code

ENTRYPOINT python server.py &>>log/log