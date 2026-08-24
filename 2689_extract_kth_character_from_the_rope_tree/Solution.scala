// LeetCode 2689 - Extract Kth Character From The Rope Tree
// https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/

class RopeTreeNode(_len: Int = 0, _value: Char = '\u0000') {
  var len: Int = _len
  var value: Char = _value
  var left: RopeTreeNode = null
  var right: RopeTreeNode = null
}

object Solution {
  def getKthCharacter(root: RopeTreeNode, k: Int): Char = dfs(root, k)

  private def dfs(node: RopeTreeNode, kk: Int): Char = {
    if (node.left == null && node.right == null) return node.value
    var leftLen = 0
    if (node.left != null) leftLen = if (node.left.len > 0) node.left.len else 1
    if (kk <= leftLen) dfs(node.left, kk)
    else dfs(node.right, kk - leftLen)
  }
}
