import web
import demjson
import Heartbeat

urls = ('/cal', 'cal')

class cal:
	def POST(self):
		data = demjson.decode(web.input()['data'])
		freq = float(web.input()['freq'])
		web.header('content-type','application/json')
		heartbeat = Heartbeat.cal(data, freq)
		print 'heartbeat is ', heartbeat
		return demjson.encode({'heartbeat':heartbeat})

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()