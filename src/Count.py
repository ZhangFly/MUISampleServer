import numpy as np
from scipy import fftpack

def execute(context):
	
	if not context.data is None \
		and not context.freq is None:

		context.data = fftpack.fft(context.data)
		index = np.argmax(context.data[0 : context.data.size / 2])
		context.result = index * context.freq * 60.0 / context.data.size
		context.prev = __name__