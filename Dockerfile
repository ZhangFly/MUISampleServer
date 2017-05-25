FROM python:2.7

RUN pip install importlib
RUN pip install demjson
RUN pip install web.py
RUN pip install PyWavelets
RUN pip install pyYaml
RUN pip install SciPy

ADD /src /code
COPY python-etcd-0.4.5 /python-etcd-0.4.5

WORKDIR /python-etcd-0.4.5
RUN python setup.py install

WORKDIR /code

ENTRYPOINT python server.py 5150