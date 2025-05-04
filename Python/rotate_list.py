"""
    2018/08/07
    Rotate List: https://leetcode.com/problems/rotate-list/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        ptr = head
        total = 0
        while ptr != None:
            ptr = ptr.next
            total += 1
        rtime = k % total if total != 0 else 0
        
        return rotate(head, total, rtime)

def rotate(head, total, k):
    if head == None or head.next == None or k == 0:
        return head
    cnt = 0
    newhead = ListNode(None)
    ptr = head
    while ptr != None:
        cnt += 1
        if total-cnt == k:
            newhead = ptr.next
            ptr.next = None
            break
        ptr = ptr.next
    ptr = newhead
    while ptr != None:
        if ptr.next == None:
            ptr.next = head
            break
        ptr = ptr.next
    
    return newhead
