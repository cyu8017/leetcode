// LeetCode 0971 - Flip Binary Tree To Match Preorder Traversal
// https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def flipMatchVoyage(root: TreeNode, voyage: Array[Int]): List[Int] = {
    var i = 0
    val ans = scala.collection.mutable.ListBuffer[Int]()
    def dfs(node: TreeNode): Boolean = {
      if (node == null) return true
      if (node.value != voyage(i)) return false
      i += 1
      if (node.left != null && node.left.value != voyage(i)) {
        ans += node.value
        return dfs(node.right) && dfs(node.left)
      }
      dfs(node.left) && dfs(node.right)
    }
    if (dfs(root)) ans.toList else List(-1)
  }
}
