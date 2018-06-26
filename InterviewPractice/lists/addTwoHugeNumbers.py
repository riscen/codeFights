# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):
    sumStr = str(int(getNumStr(a))+int(getNumStr(b)))
    if len(sumStr)%4 != 0:
        sumStr = fillNumber(sumStr, len(sumStr)+(4-len(sumStr)%4))
    i = len(sumStr)
    l = []
    while i > 0:
        num = sumStr[i-4: i]
        while num[0] == '0' and len(num) > 1:
            num = num[1:]
        l.insert(0, int(num))
        i -= 4
    return l

def getNumStr(l):
    numStr = ''
    while l:
        numStr = numStr + fillNumber(str(l.value), 4)
        l = l.next
    return numStr

def fillNumber(numStr, length):
    while len(numStr) < length:
        numStr = '0' + numStr
    return numStr