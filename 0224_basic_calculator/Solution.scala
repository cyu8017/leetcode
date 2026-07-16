// LeetCode 0224 - Basic Calculator
// https://leetcode.com/problems/basic-calculator/

import scala.collection.mutable

object Solution {
  def calculate(s: String): Int = {
    val stack = mutable.ArrayStack[Int]()
    var result = 0
    var number = 0
    var sign = 1
    for (ch <- s) {
      if (ch.isDigit) {
        number = number * 10 + (ch - '0')
      } else if (ch == '+' || ch == '-') {
        result += sign * number
        number = 0
        sign = if (ch == '+') 1 else -1
      } else if (ch == '(') {
        stack.push(result)
        stack.push(sign)
        result = 0
        sign = 1
      } else if (ch == ')') {
        result += sign * number
        number = 0
        result *= stack.pop()
        result += stack.pop()
      }
    }
    result + sign * number
  }
}
