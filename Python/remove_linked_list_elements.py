'''
    2018/11/09
    Remove Linked List Elements: https://leetcode.com/problems/remove-linked-list-elements/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pre = phead = ListNode(None)
        pre.next = head
        while head != None:
            if head.val == val:
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        
        return phead.next
