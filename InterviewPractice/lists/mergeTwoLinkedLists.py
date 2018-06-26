# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    l3 = []
    index = 0
    while l1 or l2:
        if l1 and l2:
            if l1.value < l2.value:
                l3.insert(index, l1.value)
                l1 = l1.next
            else:
                l3.insert(index, l2.value)
                l2 = l2.next
        elif l1:
            l3.insert(index, l1.value)
            l1 = l1.next
        elif l2:
            l3.insert(index, l2.value)
            l2 = l2.next            
        index += 1
    return l3
