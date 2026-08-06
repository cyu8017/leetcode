object Solution {
  def isValidSequence(root: TreeNode, arr: Array[Int]): Boolean = {
    def visit(node: TreeNode, index: Int): Boolean = {
      if (node == null || index == arr.length || node.value != arr(index)) false
      else if (node.left == null && node.right == null) index == arr.length - 1
      else visit(node.left, index + 1) || visit(node.right, index + 1)
    }
    visit(root, 0)
  }
}
