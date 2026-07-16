// LeetCode 0549 - Binary Tree Longest Consecutive Sequence II
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def longestConsecutive(root: TreeNode): Int = {
    var best = 0

    def dfs(node: TreeNode): (Int, Int) = {
      if (node == null) {
        return (0, 0)
      }

      val (leftInc, leftDec) = dfs(node.left)
      val (rightInc, rightDec) = dfs(node.right)

      var inc = 1
      var dec = 1

      if (node.left != null) {
        if (node.left.value == node.value + 1) {
          inc = math.max(inc, leftInc + 1)
        } else if (node.left.value == node.value - 1) {
          dec = math.max(dec, leftDec + 1)
        }
      }
      if (node.right != null) {
        if (node.right.value == node.value + 1) {
          inc = math.max(inc, rightInc + 1)
        } else if (node.right.value == node.value - 1) {
          dec = math.max(dec, rightDec + 1)
        }
      }

      if (node.left != null && node.right != null) {
        if (node.left.value + 1 == node.value && node.value == node.right.value - 1) {
          best = math.max(best, leftDec + 1 + rightInc)
        }
        if (node.left.value - 1 == node.value && node.value == node.right.value + 1) {
          best = math.max(best, leftInc + 1 + rightDec)
        }
      }

      best = math.max(best, math.max(inc, dec))
      (inc, dec)
    }

    dfs(root)
    best
  }
}
