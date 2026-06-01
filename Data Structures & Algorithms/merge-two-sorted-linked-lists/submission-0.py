# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Ensure that we always start merge with list1
        if list2.val < list1.val:
            list1, list2 = list2, list1

        head = ListNode(0, list1)
        curr = head.next
        list1 = list1.next
        # check list1 then check list 2 find min and append to curr
        while list1 and list2:
            if list1.val < list2.val:
                temp = list1.next
                curr.next = list1
                list1 = temp
            else:
                temp = list2.next
                curr.next = list2
                list2 = temp
            curr = curr.next
        
        if not list1:
            curr.next = list2
        if not list2:
            curr.next = list1

        return head.next
        
