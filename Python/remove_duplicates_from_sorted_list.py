'''
    2018/08/13
    Remove Duplicates from Sorted List: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr = head
        prev = ListNode(None)
        while ptr != None:
            if prev.val != ptr.val:
                prev = ptr
            ptr = ptr.next
            if ptr != None:
                if ptr.val == prev.val:
                    prev.next = ptr.next
        
        return head
