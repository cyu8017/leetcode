object Solution {
  def getLonelyNodes(root: TreeNode): List[Int] = {
    val answer = scala.collection.mutable.ListBuffer.empty[Int]
    def dfs(node: TreeNode): Unit = if (node != null) {
      if ((node.left == null) != (node.right == null)) answer += (if (node.left != null) node.left.value else node.right.value)
      dfs(node.left)
      dfs(node.right)
    }
    dfs(root)
    answer.toList
  }
}
