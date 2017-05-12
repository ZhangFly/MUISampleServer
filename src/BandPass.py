from scipy import signal

def execute(context):
	
	if not context.data is None \
		and not context.freq is None:

		N = context.data.size
		T = context.freq
		b, a = signal.butter(4, [0.02, 0.1], 'band')
		context.data = signal.lfilter(b, a, context.data)
		context.prev = __name__