# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):
    if not l or n == 0:
        return l
    lastNode = l
    totalNodes = 0
    while lastNode and lastNode.next:
        totalNodes += 1
        lastNode = lastNode.next
    
    if totalNodes == n-1:
        return l
        
    aux = l
    tail = None
    head = l
    i = 0
    while aux:
        if i == totalNodes-n:
            tail = aux
            head = aux.next
            break
        i += 1
        aux = aux.next
    
    if tail:
        tail.next = None
    lastNode.next = l
    return head
        
