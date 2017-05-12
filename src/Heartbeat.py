from Support import Context
import Workflow

def cal(data, freq=60.0):

	context = Context(data=data, freq=freq)

	Workflow.work_as_yaml(name='heartbeat', file_name='./heartbeat-workflow.yaml', context=context)

	return context.result