class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        def dfs(Node,currsum):
            if not Node :
                return False
            currsum+=Node.val
            if not Node.left and not Node.right:
                return targetSum==currsum
            
            return dfs(Node.left,currsum) or dfs(Node.right,currsum)
        return dfs(root,0)
