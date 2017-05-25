import demjson
import yaml
# import etcd

class Context:

	def __init__(self, data, freq):
		self.data = data
		self.freq = freq
		self.cA6 = []
		self.cD5 = []
		self.cD4 = []
		self.cD3 = []
		self.cD2 = []
		self.cD1 = []
		self.result = None
		self.prev = None

	def brief(self):
		return demjson.encode({'data.size' : len(self.data), \
								'freq' : self.freq, \
								'cA6.size' : len(self.cA6), \
								'cD5.size' : len(self.cD5), \
								'cD4.size' : len(self.cD4), \
								'cD3.size' : len(self.cD3), \
								'cD2.size' : len(self.cD2), \
								'cD1.size' : len(self.cD1), \
								'result' : self.result})

def load_yaml(file_name):
	file = open(file_name)
	yaml_file = yaml.load(file)
	file.close
	return yaml_file

# def load_etcd(key):
# 	client = etcd.Client(host='zhangfly.xin', protocol='http', port=2379, version_prefix='/v2')
# 	etcd_data = demjson.decode(client.read(key).value)
# 	print etcd_data
# 	return etcd_data

