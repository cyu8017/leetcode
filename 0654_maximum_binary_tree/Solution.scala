// LeetCode 0654 - Maximum Binary Tree
// https://leetcode.com/problems/maximum-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def constructMaximumBinaryTree(nums: Array[Int]): TreeNode = {
    def build(left: Int, right: Int): TreeNode = {
      if (left > right) return null
      var mid = left
      var i = left
      while (i <= right) {
        if (nums(i) > nums(mid)) mid = i
        i += 1
      }
      new TreeNode(nums(mid), build(left, mid - 1), build(mid + 1, right))
    }
    build(0, nums.length - 1)
  }
}
