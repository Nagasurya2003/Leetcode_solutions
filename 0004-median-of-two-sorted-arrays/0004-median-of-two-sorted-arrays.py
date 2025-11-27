class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=nums1+nums2
        num.sort()
        a=len(num)//2
        if len(num)%2==0:
            m=(num[a-1]+num[a])/2
            return m
        else:
            m=num[a]
            return m


        