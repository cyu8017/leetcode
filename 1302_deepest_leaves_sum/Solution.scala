// LeetCode 1302 - Deepest Leaves Sum
// https://leetcode.com/problems/deepest-leaves-sum/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def deepestLeavesSum(root: TreeNode): Int = {
    var level = List(root).filter(_ != null)
    var answer = 0
    while (level.nonEmpty) {
      answer = level.map(_.value).sum
      level = level.flatMap(n => List(n.left, n.right).filter(_ != null))
    }
    answer
  }
}
