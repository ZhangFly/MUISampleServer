import Heartbeat
from Support import load_yaml

step = 1
freq= 60.0
file_name='/Users/zfly/Documents/MUISample/Matlab/data/05-08_09-46-13.yml'

data = load_yaml(file_name)['Content']['Z'][1024 * step : 2047 + 1024 * step]

print "Data size is", len(data)
print data

heartbeat = Heartbeat.cal(data=data, freq=freq)

print "Heartbeat is", heartbeat