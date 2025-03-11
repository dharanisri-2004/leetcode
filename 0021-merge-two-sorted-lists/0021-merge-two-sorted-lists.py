# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, lst1: Optional[ListNode], lst2: Optional[ListNode]) -> Optional[ListNode]:
        if not lst1 or not lst2:
            return lst1 if lst1 else lst2
        if lst1.val>lst2.val:
            lst1,lst2=lst2,lst1
        lst1.next=self.mergeTwoLists(lst1.next,lst2)
        return lst1