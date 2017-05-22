import web
import demjson
import Heartbeat
import uuid

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
		return uuid.uuid1()

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()