// LeetCode 0872 - Leaf-Similar Trees
// https://leetcode.com/problems/leaf-similar-trees/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def leafSimilar(root1: TreeNode, root2: TreeNode): Boolean = {
    def leaves(node: TreeNode): List[Int] = {
      val result = scala.collection.mutable.ListBuffer.empty[Int]
      def dfs(cur: TreeNode): Unit = {
        if (cur == null) return
        if (cur.left == null && cur.right == null) {
          result += cur.value
          return
        }
        dfs(cur.left)
        dfs(cur.right)
      }
      dfs(node)
      result.toList
    }
    leaves(root1) == leaves(root2)
  }
}
