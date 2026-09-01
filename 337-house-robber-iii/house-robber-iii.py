class Solution(object):
    def rob(self, root):

        def solve(node):
            if not node:
                return (0, 0)

            left = solve(node.left)
            right = solve(node.right)

            rob = node.val + left[1] + right[1]

            not_rob = max(left) + max(right)

            return (rob, not_rob)

        return max(solve(root))