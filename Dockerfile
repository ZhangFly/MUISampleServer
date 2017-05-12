FROM python:2.7

RUN pip install importlib
RUN pip install demjson
RUN pip install web.py
RUN pip install PyWavelets
RUN pip install pyYaml
RUN pip install SciPy

ADD /src /code
WORKDIR /code
RUN mkdir /code/log

ENTRYPOINT python server.py