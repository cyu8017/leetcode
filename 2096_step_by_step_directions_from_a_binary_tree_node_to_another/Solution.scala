// LeetCode 2096 - Step-By-Step Directions From a Binary Tree Node to Another
// https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  private def path(node: TreeNode, target: Int, p: StringBuilder): Boolean = {
    if (node == null) return false
    if (node.value == target) return true
    p.append('L')
    if (path(node.left, target, p)) return true
    p.setCharAt(p.length - 1, 'R')
    if (path(node.right, target, p)) return true
    p.setLength(p.length - 1)
    false
  }

  def getDirections(root: TreeNode, startValue: Int, destValue: Int): String = {
    val ps = new StringBuilder
    val pd = new StringBuilder
    path(root, startValue, ps)
    path(root, destValue, pd)
    var i = 0
    while (i < ps.length && i < pd.length && ps.charAt(i) == pd.charAt(i)) i += 1
    val ans = new StringBuilder
    var k = 0
    while (k < ps.length - i) {
      ans.append('U')
      k += 1
    }
    ans.append(pd.substring(i))
    ans.toString
  }
}
