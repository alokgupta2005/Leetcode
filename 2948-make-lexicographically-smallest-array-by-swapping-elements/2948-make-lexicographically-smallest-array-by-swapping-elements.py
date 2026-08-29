class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        arr = sorted((nums[i], i) for i in range(n))

        groups = []
        current = [arr[0]]

        for i in range(1, n):
            if arr[i][0] - arr[i - 1][0] <= limit:
                current.append(arr[i])
            else:
                groups.append(current)
                current = [arr[i]]

        groups.append(current)

        ans = nums[:]

        for group in groups:
            values = [x[0] for x in group]
            indices = sorted(x[1] for x in group)
            for idx, value in zip(indices, values):
                ans[idx] = value

        return ans