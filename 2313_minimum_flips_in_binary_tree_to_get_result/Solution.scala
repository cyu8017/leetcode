// LeetCode 2313 - Minimum Flips in Binary Tree to Get Result
// https://leetcode.com/problems/minimum-flips-in-binary-tree-to-get-result/

class TreeNode(var value: Int = 0, var left: TreeNode = null, var right: TreeNode = null)

object Solution {
  def minimumFlips(root: TreeNode, result: Boolean): Int = {
    val res = dfs(root)
    if (result) res(1) else res(0)
  }

  private def dfs(node: TreeNode): Array[Int] = {
    if (node.left == null && node.right == null) {
      return if (node.value == 0) Array(0, 1) else Array(1, 0)
    }
    if (node.value == 5) {
      val x = dfs(node.left)
      return Array(x(1), x(0))
    }
    val L = dfs(node.left)
    val R = dfs(node.right)
    val lf = L(0)
    val lt = L(1)
    val rf = R(0)
    val rt = R(1)
    if (node.value == 2) {
      return Array(lf + rf, math.min(lt + rt, math.min(lt + rf, lf + rt)))
    }
    if (node.value == 3) {
      return Array(math.min(lf + rf, math.min(lf + rt, lt + rf)), lt + rt)
    }
    if (node.value == 4) {
      return Array(math.min(lf + rf, lt + rt), math.min(lf + rt, lt + rf))
    }
    Array(0, 0)
  }
}
