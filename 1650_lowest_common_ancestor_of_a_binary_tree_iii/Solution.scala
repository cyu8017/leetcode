// LeetCode 1650 - Lowest Common Ancestor of a Binary Tree III
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

class Node(var value: Int = 0, var left: Node = null, var right: Node = null, var parent: Node = null)

object Solution {
  def lowestCommonAncestor(p: Node, q: Node): Node = {
    var a = p
    var b = q
    while (a ne b) {
      a = if (a != null) a.parent else q
      b = if (b != null) b.parent else p
    }
    a
  }
}
