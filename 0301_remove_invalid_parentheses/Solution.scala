// LeetCode 0301 - Remove Invalid Parentheses
// https://leetcode.com/problems/remove-invalid-parentheses/

import scala.collection.mutable

object Solution {
  def removeInvalidParentheses(s: String): List[String] = {
    val result = mutable.Set.empty[String]
    val queue = mutable.Queue.empty[String]
    val visited = mutable.Set.empty[String]
    queue.enqueue(s)
    visited.add(s)
    var found = false
    while (queue.nonEmpty) {
      val levelSize = queue.size
      var step = 0
      while (step < levelSize) {
        val current = queue.dequeue()
        if (isValid(current)) {
          result.add(current)
          found = true
        }
        if (!found) {
          var index = 0
          while (index < current.length) {
            if (current(index) == '(' || current(index) == ')') {
              val next = current.substring(0, index) + current.substring(index + 1)
              if (visited.add(next)) {
                queue.enqueue(next)
              }
            }
            index += 1
          }
        }
        step += 1
      }
    }
    result.toList
  }

  private def isValid(text: String): Boolean = {
    var balance = 0
    var index = 0
    while (index < text.length) {
      text(index) match {
        case '(' => balance += 1
        case ')' =>
          if (balance == 0) {
            return false
          }
          balance -= 1
        case _ =>
      }
      index += 1
    }
    balance == 0
  }
}
