// LeetCode 0536 - Construct Binary Tree from String
// https://leetcode.com/problems/construct-binary-tree-from-string/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def str2tree(s: String): TreeNode = {
    if (s == null || s.isEmpty) {
      return null
    }
    var index = 0

    def parse(): TreeNode = {
      if (index >= s.length) {
        return null
      }

      var sign = 1
      if (s(index) == '-') {
        sign = -1
        index += 1
      }

      var value = 0
      while (index < s.length && s(index).isDigit) {
        value = value * 10 + (s(index) - '0')
        index += 1
      }

      val node = new TreeNode(sign * value)

      if (index < s.length && s(index) == '(') {
        index += 1
        node.left = parse()
        index += 1
      }

      if (index < s.length && s(index) == '(') {
        index += 1
        node.right = parse()
        index += 1
      }

      node
    }

    parse()
  }
}
