"""
Unit test script for Lab 13

Authors: Walker M. White (wmw2), Lillian Lee (ljl2)
Date:    October 17, 2019
"""
import recursion


def testSumList():
    """
    Tests for function sum_list
    """
    print('Testing sum_list')
    assert (0 ==  recursion.sumList([]))
    assert (34 == recursion.sumList([34]))
    assert (46 == recursion.sumList([7,34,1,2,2]))


def testNumberOf():
    """
    Tests for function numberof
    """
    print('Testing numberof')
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    assert(1 == recursion.numberOf([4],4))
    assert(0 == recursion.numberOf([],4))
    assert(3 == recursion.numberOf(mylist,74))
    assert(2 == recursion.numberOf(mylist,3))
    assert(0 == recursion.numberOf(mylist,4))


#Test Cases for Optional Functions
def testNumberNot():
    """
    Tests for function number_not
    """
    print('Testing number_not')
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    assert(0 == recursion.numberNot([],4))
    assert(0 == recursion.numberNot([4],4))
    assert(4 == recursion.numberNot(mylist,74))
    assert(5 == recursion.numberNot(mylist,3))
    assert(7 == recursion.numberNot(mylist,4))


def testRemoveFirst():
    """
    Tests for function remove_first
    """
    print('Testing remove_first')
    assert([] == recursion.removeFirst([],3))
    assert([] == recursion.removeFirst([3],3))
    assert([3] == recursion.removeFirst([3],4))
    assert([3, 4, 4, 5]  == recursion.removeFirst([3, 4, 4, 4, 5],4))
    assert([3, 5, 4, 4, 4] == recursion.removeFirst([3, 4, 5, 4, 4, 4],4))


# Script Code
if __name__ == '__main__':
    testSumList()
    testNumberOf()
    testNumberNot()
    #testRemoveFirst()

    print('all tests passed.')