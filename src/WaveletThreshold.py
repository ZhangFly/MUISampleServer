import pywt as pw

def execute(context):
	
	if not context.cD5 is None:
		context.cD5 = pw.threshold(context.cD5, 0.006, 'soft')

	if not context.cD4 is None:
		context.cD4 = pw.threshold(context.cD4, 0.01, 'soft')
	
	if not context.cD4 is None:
		context.cD3 = pw.threshold(context.cD3, 0.018, 'soft')
	
	if not context.cD4 is None:
		context.cD2 = pw.threshold(context.cD2, 0.018, 'soft')

	if not context.cD4 is None:
		context.cD1 = pw.threshold(context.cD1, 0.018, 'soft')
	
	context.prev = __name__