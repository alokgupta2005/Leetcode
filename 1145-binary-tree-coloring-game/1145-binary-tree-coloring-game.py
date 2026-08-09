# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def btreeGameWinningMove(
        self, root: Optional[TreeNode], n: int, x: int
    ) -> bool:

        left = 0
        right = 0

        def count(node):
            nonlocal left, right

            if not node:
                return 0

            l = count(node.left)
            r = count(node.right)

            if node.val == x:
                left = l
                right = r

            return l + r + 1

        count(root)
        parent = n - (left + right + 1)

        return max(left, right, parent) > n // 2
        