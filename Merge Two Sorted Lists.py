class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1,l2):
    if l1==None:
        return l2
    if l2==None:
        return l1
    if l1.val<=l2.val:
        l1.next=self.mergeTwoLists(l1.next,l2)
        return l1
    else:
        l2.next=self.mergeTwoLists(l1,l2.next)
        return l2