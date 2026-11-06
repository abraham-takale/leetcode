# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        curr,stuck=root,[]
        res=[]
        while curr or stuck:
            if curr:
                res.append(curr.val)
                stuck.append(curr.right)
                curr=curr.left
            else:
                curr=stuck.pop()
        return res
