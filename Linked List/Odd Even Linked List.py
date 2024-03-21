# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head1=odd=ListNode()
        head2=even=ListNode()
        t=head
        i=0
        while t:
            if i%2==0:
                even.next=t
                even=even.next
            else:
                odd.next=t
                odd=odd.next
            t=t.next
            i+=1
        odd.next=None
        even.next=head1.next
        return head2.next
        





















   
