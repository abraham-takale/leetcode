# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        curr=head
        pre=None
        while curr is not None:
            next=curr.next
            curr.next=pre
            pre=curr
            curr=next
        return pre
