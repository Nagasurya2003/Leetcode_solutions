class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        min_length = min(len(s) for s in strs)
        for j in range(min_length):
            char=strs[0][j]
            for s in strs:
              if s[j] != char:
                return prefix
            prefix += char
        return prefix  



            
        