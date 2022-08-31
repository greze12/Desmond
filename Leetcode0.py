'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
EX:-
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''


def addnum(self, l1, l2, c=0):
    val = l1.val + l2.val +c
    c = val//10
    ret = ListNode(val%10)

    if(l1.next != None or l2.next != None or c != 0):
        if l1.next == None:
            l1 = ListNode(0)
            if l2.next == None:
                l2 = ListNode(0)
                ret.next = self.addnum(l1.next , l2.next , c)
                return ret

