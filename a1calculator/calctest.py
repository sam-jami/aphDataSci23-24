import calc
def testAdd ():
    assert (calc.math ("3333333 + -3") == 3333330)
def testMinus ():
    assert (calc.math ("3333333 - 3333330") == 3)
def testTimes ():
    assert (calc.math ("13 * 7") == 91)
def testDiv():
    assert (calc.math ("4000 / 40") == 100)
def testPow ():
    assert (calc.math ("2 ^ -3") == 1/8)

testAdd ()
testMinus ()
testTimes ()
testDiv ()
testPow ()

print ("all tests passed")