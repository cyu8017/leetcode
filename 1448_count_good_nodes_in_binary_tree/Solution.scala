object Solution {
  def goodNodes(root: TreeNode): Int = {
    def visit(node: TreeNode, maximum: Int): Int =
      if (node == null) 0 else (if (node.value >= maximum) 1 else 0) + visit(node.left, maximum.max(node.value)) + visit(node.right, maximum.max(node.value))
    visit(root, Int.MinValue)
  }
}
