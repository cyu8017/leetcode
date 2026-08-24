// LeetCode 3749 - Evaluate Valid Expressions
// https://leetcode.com/problems/evaluate-valid-expressions/

object Solution {
  def evaluateExpression(expression: String): Long = {
    def parse(i0: Int): Array[Long] = {
      val ch = expression.charAt(i0)
      if (Character.isDigit(ch) || ch == '-') {
        var j = i0
        if (expression.charAt(j) == '-') j += 1
        while (j < expression.length && Character.isDigit(expression.charAt(j))) j += 1
        return Array(java.lang.Long.parseLong(expression.substring(i0, j)), j.toLong)
      }
      var j = i0
      while (expression.charAt(j) != '(') j += 1
      val op = expression.substring(i0, j)
      j += 1
      val p1 = parse(j)
      j = p1(1).toInt + 1
      val p2 = parse(j)
      j = p2(1).toInt + 1
      var res = 0L
      if (op == "add") res = p1(0) + p2(0)
      else if (op == "sub") res = p1(0) - p2(0)
      else if (op == "mul") res = p1(0) * p2(0)
      else if (op == "div") res = p1(0) / p2(0)
      Array(res, j.toLong)
    }
    parse(0)(0)
  }
}
