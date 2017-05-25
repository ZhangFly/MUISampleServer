from Support import load_yaml
# from Support import load_etcd
import importlib

def do_work(config, context):
	works = []
	first = None
	last = None
	before = None
	after = None

	if config.has_key('works'):
		for work_name in config['works']:
			works.append(importlib.import_module(work_name))

	if config.has_key('first'):
		first = importlib.import_module(config['first'])

	if config.has_key('last'):
		last = importlib.import_module(config['last'])

	if config.has_key('before'):
		before = importlib.import_module(config['before'])

	if config.has_key('after'):
		after = importlib.import_module(config['after'])

	if not first is None:
		first.execute(context)

	for work in works:
		if not before is None:
			before.execute(context)

		work.execute(context)

		if not after is None:
			after.execute(context)

	if not last is None:
		last.execute(context)

	return context.result

# def work_as_etcd(file_name, context):
# 	config = load_etcd(key=file_name)
# 	return do_work(config, context)

def work_as_yaml(file_name, context):
	config = load_yaml(file_name=file_name)
	return do_work(config, context)
	

