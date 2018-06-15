# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    aux = l
    aux_prev = None
    while aux:
        if aux.value == k:
            if aux_prev != None:
                aux_prev.next = aux.next
            else:
                l = aux.next
            aux = aux.next 
        else:
            aux_prev = aux
            aux = aux.next        
    return l