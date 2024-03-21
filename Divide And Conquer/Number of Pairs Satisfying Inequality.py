# class Solution:
#     def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
#         n=len(nums1)
#         count=0
#         for i in range(n):
#             for j in range(i+1,n):
#                 diff1=nums1[i]-nums1[j]
#                 diff2=nums2[i]-nums2[j]+diff
#                 if diff1<=diff2:
#                     count+=1
#         return count
from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        N = len(nums1)
        count = 0
        sl = SortedList()
        
        for i in range(N):
		

            count += sl.bisect_right(nums1[i]-nums2[i]+diff)
			

            sl.add(nums1[i] - nums2[i])
			
        return count

        
