# Leetcode 142: Linked list cycle II
# Difficulty : Medium
# Language : Python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        # step 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
            # step 2: Find the starting node of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow 
