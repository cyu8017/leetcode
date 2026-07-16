// LeetCode 0439 - Ternary Expression Parser
// https://leetcode.com/problems/ternary-expression-parser/

object Solution {
  def parseTernary(expression: String): String = {
    if (!expression.contains("?")) {
      return expression
    }

    var separator = 2
    var depth = 0
    for (index <- 2 until expression.length) {
      expression(index) match {
        case '?' => depth += 1
        case ':' =>
          if (depth == 0) {
            separator = index
            return if (expression(0) == 'T') {
              parseTernary(expression.substring(2, separator))
            } else {
              parseTernary(expression.substring(separator + 1))
            }
          } else {
            depth -= 1
          }
        case _ =>
      }
    }

    if (expression(0) == 'T') {
      parseTernary(expression.substring(2, separator))
    } else {
      parseTernary(expression.substring(separator + 1))
    }
  }
}
