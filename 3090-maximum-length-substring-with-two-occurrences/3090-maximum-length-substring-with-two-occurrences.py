class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        freq = {}
        ans = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans