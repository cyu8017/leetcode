// LeetCode 0227 - Basic Calculator II
// https://leetcode.com/problems/basic-calculator-ii/

import scala.collection.mutable

object Solution {
  def calculate(s: String): Int = {
    val stack = mutable.ArrayDeque.empty[Int]
    var number = 0
    var operator = '+'

    for (index <- s.indices) {
      val ch = s(index)
      if (ch.isDigit) {
        number = number * 10 + (ch - '0')
      }
      if (ch == '+' || ch == '-' || ch == '*' || ch == '/' || index == s.length - 1) {
        operator match {
          case '+' => stack.append(number)
          case '-' => stack.append(-number)
          case '*' => stack.append(stack.removeLast() * number)
          case '/' => stack.append(stack.removeLast() / number)
        }
        operator = ch
        number = 0
      }
    }

    stack.sum
  }
}
