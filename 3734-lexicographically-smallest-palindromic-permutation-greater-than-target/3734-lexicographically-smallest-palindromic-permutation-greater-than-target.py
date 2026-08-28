from collections import Counter
from typing import Optional, Dict


class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        odd_chars = [c for c, v in counts.items() if v % 2 == 1]

        
        if len(odd_chars) > 1:
            return ""

        half_len = n // 2
        mid_char = odd_chars[0] if odd_chars else None
        half_counts = {c: v // 2 for c, v in counts.items() if v // 2 > 0}

        def build(H: str) -> str:
            mid = mid_char if mid_char is not None else ""
            return H + mid + H[::-1]

        target_head = target[:half_len]

        if Counter(target_head) == Counter(half_counts):
            candidate = build(target_head)
            if candidate > target:
                return candidate

        H = self._smallest_strictly_greater(half_counts, target_head)
        if H is not None:
            return build(H)

        return ""

    @staticmethod
    def _smallest_strictly_greater(counts: Dict[str, int], target_str: str) -> Optional[str]:
        """Smallest permutation of the multiset `counts` that is strictly
        greater than target_str (same length), or None if impossible.
        Iterative (no recursion) -> safe for large n.
        """
        counts = dict(counts)
        n = len(target_str)

        last_fallback = None  # (position, char_to_use, counts_snapshot_before_position)
        matched_fully = True

        for i in range(n):
            tc = target_str[i]
            # chars strictly greater than tc that are still available
            greater_chars = sorted(c for c, v in counts.items() if v > 0 and c > tc)
            if greater_chars:
                last_fallback = (i, greater_chars[0], dict(counts))

            if counts.get(tc, 0) > 0:
                counts[tc] -= 1
            else:
                matched_fully = False
                break
        # if loop completes fully, H == target_str exactly -> NOT strictly greater
        # either way (full match or mismatch), we must use the last fallback point

        if last_fallback is None:
            return None

        pos, ch, snapshot = last_fallback
        snapshot[ch] -= 1

        remaining = []
        for c in sorted(snapshot):
            remaining.extend([c] * snapshot[c])

        return target_str[:pos] + ch + "".join(remaining)