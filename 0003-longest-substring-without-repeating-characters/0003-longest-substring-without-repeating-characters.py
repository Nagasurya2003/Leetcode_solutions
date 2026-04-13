class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        maxi = 0

        for right in range(len(s)):
            
            # If duplicate, shrink window
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add current character
            char_set.add(s[right])
            
            # Update max length
            maxi = max(maxi, right - left + 1)

        return maxi