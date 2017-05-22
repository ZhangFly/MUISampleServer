import web
import demjson
import Heartbeat
import os

urls = ('/cal', 'cal')

class cal:
	def POST(self):
		data = demjson.decode(web.input()['data'])
		freq = float(web.input()['freq'])
		web.header('content-type','application/json')
		heartbeat = Heartbeat.cal(data, freq)
		print 'heartbeat is ', heartbeat
		return demjson.encode({'heartbeat':heartbeat})

class cal:
	def GET(self):
		output = os.popen('ifconfig |grep inet')
		return output.read()

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()