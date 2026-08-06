// LeetCode 1597 - Build Binary Expression Tree From Infix Expression
// https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/

class Node(_val: String = " ", _left: Node = null, _right: Node = null) {
  var `val`: String = _val
  var left: Node = _left
  var right: Node = _right
}

object Solution {
  def expTree(s: String): Node = {
    val nodes = scala.collection.mutable.Stack.empty[Node]
    val ops = scala.collection.mutable.Stack.empty[Char]
    val priority = Map('+' -> 1, '-' -> 1, '*' -> 2, '/' -> 2)
    def applyOp(): Unit = {
      val op = ops.pop()
      val right = nodes.pop()
      val left = nodes.pop()
      nodes.push(new Node(op.toString, left, right))
    }
    for (ch <- s) {
      if (ch.isDigit) nodes.push(new Node(ch.toString))
      else if (ch == '(') ops.push(ch)
      else if (ch == ')') {
        while (ops.top != '(') applyOp()
        ops.pop()
      } else {
        while (ops.nonEmpty && ops.top != '(' && priority(ops.top) >= priority(ch)) applyOp()
        ops.push(ch)
      }
    }
    while (ops.nonEmpty) applyOp()
    nodes.pop()
  }
}
