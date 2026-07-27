// LeetCode 1612 - Check If Two Expression Trees are Equivalent
// https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/

class Node(_val: String = "", _left: Node = null, _right: Node = null) {
  var `val`: String = _val
  var left: Node = _left
  var right: Node = _right
}

object Solution {
  def checkEquivalence(root1: Node, root2: Node): Boolean = {
    def count(node: Node, out: Array[Int]): Unit = {
      if (node == null) return
      if (node.`val` == "+") {
        count(node.left, out)
        count(node.right, out)
      } else {
        out(node.`val`.charAt(0) - 'a') += 1
      }
    }
    val a = Array.fill(26)(0)
    val b = Array.fill(26)(0)
    count(root1, a)
    count(root2, b)
    a.sameElements(b)
  }
}
