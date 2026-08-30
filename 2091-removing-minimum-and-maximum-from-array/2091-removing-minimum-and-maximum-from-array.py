class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        if min_idx > max_idx:
            min_idx, max_idx = max_idx, min_idx
        option1 = max_idx + 1
        option2 = n - min_idx
        option3 = (min_idx + 1) + (n - max_idx)

        return min(option1, option2, option3)