// LeetCode 1522 - Diameter of N-Ary Tree
// https://leetcode.com/problems/diameter-of-n-ary-tree/

class Node(_value: Int = 0, _children: List[Node] = Nil) {
  var value: Int = _value
  var children: List[Node] = _children
}

object Solution {
  def diameter(root: Node): Int = {
    var answer = 0
    def depth(node: Node): Int = {
      var longest = 0
      var second = 0
      for (child <- node.children) {
        val value = depth(child) + 1
        if (value > longest) {
          second = longest
          longest = value
        } else if (value > second) second = value
      }
      answer = math.max(answer, longest + second)
      longest
    }
    if (root != null) depth(root)
    answer
  }
}
