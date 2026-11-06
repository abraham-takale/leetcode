class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        curr,stack=root,[]
        res=[]
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.left)
                curr=curr.right
            else:
                curr=stack.pop()
        return res[::-1]
