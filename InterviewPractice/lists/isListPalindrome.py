# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    if not l:
        return True
    auxList = []
    while l:
        auxList.append(l.value)
        l = l.next
    i = 0
    j = len(auxList)-1
    while i < j:
        if auxList[i] != auxList[j]:
            return False
        i += 1
        j -= 1
    return True