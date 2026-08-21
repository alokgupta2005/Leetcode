class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def count(x):
            from math import gcd

            n = len(coins)
            ans = 0

            def lcm(a, b):
                return a // gcd(a, b) * b

            for mask in range(1, 1 << n):
                value = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        value = lcm(value, coins[i])

                        if value > x:
                            valid = False
                            break

                if valid:
                    if bits % 2 == 1:
                        ans += x // value
                    else:
                        ans -= x // value

            return ans

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left