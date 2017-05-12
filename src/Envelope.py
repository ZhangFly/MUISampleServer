import numpy as np
from scipy import signal
from scipy import fftpack

def execute(context):

	if not context.data is None:
		context.data = np.sqrt(context.data**2 + fftpack.hilbert(context.data)**2)

	context.prev = __name__