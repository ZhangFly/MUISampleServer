import web
import demjson
import Heartbeat
import uuid

urls = ('/cal', 'cal')

class cal:

	ustr = None

	def POST(self):
		data = demjson.decode(web.input()['data'])
		freq = float(web.input()['freq'])
		web.header('content-type','application/json')
		heartbeat = Heartbeat.cal(data, freq)
		print 'heartbeat is ', heartbeat
		return demjson.encode({'heartbeat':heartbeat})

	def GET(self):
		if cal.ustr is None:
			cal.ustr = uuid.uuid1()
		return cal.ustr

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()