from Support import Context
import Workflow

def cal(data, freq=60.0):

	context = Context(data=data, freq=freq)

	# Workflow.work_as_yaml(file_name='./heartbeat-workflow.yaml', context=context)
	Workflow.work_as_etcd(file_name='heartbeat', context=context)

	return context.result