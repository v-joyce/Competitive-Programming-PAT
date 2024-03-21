# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # left=right=head
        # c1,c2=0,0
        # n=0
        # while c1<k:
        #     left=left.next
        #     c2+=1
        #     temp=head
        #     while c2<n-k:
        #         right=right.next
        #         c2-=1
        #     while temp:
        #         temp=temp.next
        #         n1=1
        #     t=left
        #     left=right
        #     right=t
        #     return head
        curr=head
        for i in range(k-1):
            curr=curr.next
        left=curr
        right=head
        while curr.next:
            curr=curr.next
            right=right.next
        left.val,right.val=right.val,left.val
        return head
