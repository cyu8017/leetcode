// LeetCode 1628 - Design an Expression Tree With Evaluate Function
// https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/

abstract class Node {
  def evaluate(): Int
}

class TreeBuilder {
  private class NumNode(v: Int) extends Node {
    def evaluate(): Int = v
  }
  private class OpNode(op: String, left: Node, right: Node) extends Node {
    def evaluate(): Int = {
      val a = left.evaluate()
      val b = right.evaluate()
      op match {
        case "+" => a + b
        case "-" => a - b
        case "*" => a * b
        case "/" => a / b
      }
    }
  }

  def expTree(postfix: Array[String]): Node = {
    val stack = scala.collection.mutable.Stack.empty[Node]
    for (token <- postfix) {
      if (token == "+" || token == "-" || token == "*" || token == "/") {
        val right = stack.pop()
        val left = stack.pop()
        stack.push(new OpNode(token, left, right))
      } else {
        stack.push(new NumNode(token.toInt))
      }
    }
    stack.pop()
  }
}
