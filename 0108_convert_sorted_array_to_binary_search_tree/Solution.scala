// LeetCode 0108 - Convert Sorted Array to Binary Search Tree
// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def sortedArrayToBST(nums: Array[Int]): TreeNode = {
    def build(left: Int, right: Int): TreeNode = {
      if (left > right) {
        null
      } else {
        val mid = (left + right + 1) / 2
        val root = new TreeNode(nums(mid))
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        root
      }
    }
    build(0, nums.length - 1)
  }
}
