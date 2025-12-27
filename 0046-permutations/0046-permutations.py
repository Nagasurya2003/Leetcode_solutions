class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def rep(a):
            if len(a)==len(nums):
                res.append(a[:])
                return
            for i in nums:
                if i in a:
                    continue
                a.append(i)
                rep(a)
                a.pop()
        rep([])
        return res

        