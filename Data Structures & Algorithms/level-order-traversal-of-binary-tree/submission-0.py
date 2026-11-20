# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root == None:
            return []
        q = []
        op = []
        curr = []
        curr_height = 0
        q.append((root, 0))
        while len(q) > 0:
            node, height = q.pop(0)
            if height != curr_height:
                op.append(curr[:])
                curr = []
                curr_height = height

            curr.append(node.val)
            if node.left:
                q.append((node.left, height + 1))
            if node.right:
                q.append((node.right, height + 1))

        if len(curr) > 0:
            op.append(curr[:])

        return op