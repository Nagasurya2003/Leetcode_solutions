from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        for key in d:
            if d[key] == 1:
                return key