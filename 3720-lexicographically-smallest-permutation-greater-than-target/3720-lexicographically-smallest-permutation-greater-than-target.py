class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        from collections import Counter

        count = Counter(s)
        n = len(target)

        def build(pos, greater):
            if pos == n:
                return "" if greater else None
            for ch in sorted(count):
                if count[ch] == 0:
                    continue    
                if greater or ch > target[pos]:
                    count[ch] -= 1
                    suffix = build(pos + 1, True)
                    count[ch] += 1

                    if suffix is not None:
                        return ch + suffix
             
                elif ch == target[pos]:
                    count[ch] -= 1
                    suffix = build(pos + 1, False)
                    count[ch] += 1

                    if suffix is not None:
                        return ch + suffix

            return None

        ans = build(0, False)
        return ans if ans is not None else ""