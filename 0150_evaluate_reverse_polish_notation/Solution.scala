// LeetCode 0150 - Evaluate Reverse Polish Notation
// https://leetcode.com/problems/evaluate-reverse-polish-notation/

import scala.collection.mutable.Stack
object Solution {
  def evalRPN(tokens: Array[String]): Int = {
    val stack = Stack[Int]()
    tokens.foreach {
      case "+" => val right = stack.pop(); val left = stack.pop(); stack.push(left + right)
      case "-" => val right = stack.pop(); val left = stack.pop(); stack.push(left - right)
      case "*" => val right = stack.pop(); val left = stack.pop(); stack.push(left * right)
      case "/" => val right = stack.pop(); val left = stack.pop(); stack.push(left / right)
      case number => stack.push(number.toInt)
    }
    stack.top
  }
}