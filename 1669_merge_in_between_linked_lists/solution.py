class ListNode:
    def __init__(self, val=0, next=None):
        self.val,self.next=val,next
class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        pre=list1
        for _ in range(a-1):pre=pre.next
        post=pre
        for _ in range(b-a+2):post=post.next
        pre.next=list2
        while pre.next:pre=pre.next
        pre.next=post
        return list1
