class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)

        for i in range((n // 2) + 1):
            ans[2 * i] = ans[i]

            if 2 * i + 1 <= n:
                ans[2 * i + 1] = ans[i] + 1

        return ans