// LeetCode 0968 - Binary Tree Cameras
// https://leetcode.com/problems/binary-tree-cameras/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def minCameraCover(root: TreeNode): Int = {
    var cameras = 0
    def dfs(node: TreeNode): Int = {
      if (node == null) return 1
      val left = dfs(node.left)
      val right = dfs(node.right)
      if (left == 0 || right == 0) {
        cameras += 1
        return 2
      }
      if (left == 2 || right == 2) return 1
      0
    }
    val rootState = dfs(root)
    cameras + (if (rootState == 0) 1 else 0)
  }
}
