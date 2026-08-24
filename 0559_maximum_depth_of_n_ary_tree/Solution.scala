// LeetCode 0559 - Maximum Depth of N-ary Tree
// https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

class Node(_value: Int = 0, _children: List[Node] = Nil) {
  var value: Int = _value
  var children: List[Node] = _children
}

object Solution {
  def maxDepth(root: Node): Int = {
    if (root == null) return 0
    if (root.children == null || root.children.isEmpty) return 1
    var best = 0
    root.children.foreach { child =>
      best = math.max(best, maxDepth(child))
    }
    best + 1
  }
}
