class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        p = head
        c = head.next
        i = 1
        first = last = -1
        mn = float('inf')

        while c and c.next:
            if (c.val > p.val and c.val > c.next.val) or (c.val < p.val and c.val < c.next.val):
                if first == -1:
                    first = i
                else:
                    mn = min(mn, i - last)
                last = i

            p = c
            c = c.next
            i += 1

        return [-1, -1] if first == last else [mn, last - first]