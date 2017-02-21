"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

"""

def print_backward(list):
    if list == None: return
    head = list
    tail = list.next
    print_backward(tail)
    print head,

class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):

        return self.solution1(l1, l2)
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

    def solution1(self, l1, l2):
        result = self.recursiveAdd(l1, l2, 0)
        return result

    def recursiveAdd(self, l1, l2, increase):
        if l1 == None and l2 == None:
            if increase > 0:
                return ListNode(1)
            else:
                return None
        else:
            val1 = l1.val if l1 != None else 0
            val2 = l2.val if l2 != None else 0
            next1 = l1.next if l1!= None else None
            next2 = l2.next if l2!= None else None
            value = val1 + val2 + increase
            nextIncreate = 0
            if value >= 10:
                nextIncreate = 1
                value -= 10
            result = ListNode(value)
            result.next = self.recursiveAdd(next1, next2, nextIncreate)
            return result

def main():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    s = Solution()
    print_backward (s.addTwoNumbers(l1, l2))

if __name__ == '__main__':
    main()