import pywt as pw
import numpy as np

def execute(context):

	if not context.cD5 is None \
		and not context.cD4 is None \
		and not context.cD3 is None \
		and not context.cD2 is None \
		and not context.cD1 is None:

		dCoeffs = [np.zeros(72), context.cD5, context.cD4, context.cD3, context.cD2, context.cD1]
		context.data = pw.waverec(dCoeffs, 'db5')

	context.prev = __name__