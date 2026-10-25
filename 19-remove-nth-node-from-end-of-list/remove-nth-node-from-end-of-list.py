# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        current = head
        count = 0

        # First pass: count the nodes
        while current is not None:
            count += 1
            current = current.next

        # Special case: removing the head
        if count == n:
            return head.next

        # Second pass: find the node before the one to remove
        traverse = 0
        check = head

        while traverse < count - n - 1:
            check = check.next
            traverse += 1

        # Skip the node we want to remove
        check.next = check.next.next

        return head
