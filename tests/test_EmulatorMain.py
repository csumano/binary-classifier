from hypothesis import given
from binaryclassifier import EmulatorMain

def test_createError():
	error = EmulatorMain.createError()
	assert error > -0.05 and error < 0.05
