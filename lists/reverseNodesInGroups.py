# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseNodesInKGroups(l, k):
    reversedL = []
    while l:
        kList = []
        while l and len(kList) < k:
            kList.insert(0, l.value)
            l = l.next
        if len(kList) < k:
            index = len(reversedL)
            for node in kList:
                reversedL.insert(index, node)
        else:
            for node in kList:
                reversedL.append(node)
    return reversedL
        
