// LeetCode 3319 - K-th Largest Perfect Subtree Size in Binary Tree
// https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def kthLargestPerfectSubtree(root: TreeNode, k: Int): Int = {
    val sizes = scala.collection.mutable.ArrayBuffer.empty[Int]
    def dfs(node: TreeNode): Array[Int] = {
      if (node == null) return Array(0, 0, 1)
      val L = dfs(node.left)
      val R = dfs(node.right)
      val sz = L(1) + R(1) + 1
      val perf = L(2) == 1 && R(2) == 1 && L(0) == R(0)
      if (perf) sizes += sz
      Array(math.max(L(0), R(0)) + 1, sz, if (perf) 1 else 0)
    }
    dfs(root)
    val sorted = sizes.sorted.reverse
    if (k > sorted.length) -1 else sorted(k - 1)
  }
}
