// LeetCode 0700 - Search in a Binary Search Tree
// https://leetcode.com/problems/search-in-a-binary-search-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def searchBST(root: TreeNode, `val`: Int): TreeNode = {
    var node = root
    while (node != null && node.value != `val`) {
      node = if (`val` < node.value) node.left else node.right
    }
    node
  }
}
