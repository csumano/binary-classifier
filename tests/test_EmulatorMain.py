from binaryclassifier import EmulatorMain

def test_createError():
    for x in range(0, 100):
        error = EmulatorMain.createError()
        print error # Show value in case of test failure
        assert error >= -0.05 and error <= 0.05
