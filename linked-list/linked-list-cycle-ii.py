class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        check=set()
        while curr:
            if curr in check:
                return curr
            check.add(curr)
            curr=curr.next
        return None
