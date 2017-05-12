import pywt as pw

def execute(context):

	if not context.data is None:
		context.cA6, context.cD5, context.cD4, context.cD3, context.cD2, context.cD1 = pw.wavedec(context.data, 'db5', level=5)

	context.prev = __name__