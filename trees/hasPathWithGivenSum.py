#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):
    if not t and s == 0:
        return True
    elif preorder(t, s, 0):
        return True
    return False

def preorder(t, s, actualSum):
    if t and not t.left and not t.right and actualSum+t.value == s:
        return True
    elif not t:
        return False
    if preorder(t.left, s, actualSum+t.value):
        return True
    if preorder(t.right, s, actualSum+t.value):
        return True
    
    
    
    
    