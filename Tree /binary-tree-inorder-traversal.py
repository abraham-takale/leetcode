# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        curr,stuck=root,[]
        res=[]
        while curr or stuck:
            if curr:
                stuck.append(curr)
                curr=curr.left
            else:
                curr=stuck.pop()
                res.append(curr.val)
                curr=curr.right
        return res
