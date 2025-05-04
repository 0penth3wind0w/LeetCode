"""
    2018/08/01
    Add Two Numbers: https://leetcode.com/problems/add-two-numbers/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        v1 = extractValue(l1)
        v2 = extractValue(l2)
        result = str(v1 + v2)[::-1]

        return createNode(result)

def extractValue(node):
    value, expon = 0, 0
    while node != None:
        value += node.val * 10 ** expon
        node = node.next
        expon += 1

    return value

def createNode(value):
    node = ListNode(int(value[0]))
    node.next = createNode(value[1:]) if len(value[1:]) != 0 else None
    
    return node
