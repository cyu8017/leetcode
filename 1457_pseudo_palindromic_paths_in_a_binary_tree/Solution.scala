object Solution {
  def pseudoPalindromicPaths(root: TreeNode): Int = {
    def dfs(node: TreeNode, mask: Int): Int = {
      if (node == null) 0 else {
        val next = mask ^ (1 << node.value)
        if (node.left == null && node.right == null) if ((next & (next - 1)) == 0) 1 else 0
        else dfs(node.left, next) + dfs(node.right, next)
      }
    }
    dfs(root, 0)
  }
}
