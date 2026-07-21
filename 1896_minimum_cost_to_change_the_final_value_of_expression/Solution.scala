// LeetCode 1896 - Minimum Cost to Change the Final Value of Expression
// https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/

object Solution {
  def minOperationsToFlip(expression: String): Int = {
    def combine(left: Array[Int], op: Char, right: Array[Int]): Array[Int] = {
      val Array(leftVal, leftToZero, leftToOne) = left
      val Array(rightVal, rightToZero, rightToOne) = right
      if (op == '&') {
        val andVal = leftVal & rightVal
        val andToZero = math.min(leftToZero, leftToOne + rightToZero)
        val andToOne = leftToOne + rightToOne
        val orToZero = leftToZero + rightToZero
        val orToOne = math.min(leftToOne, math.min(leftToZero + rightToOne, rightToZero + leftToOne))
        Array(andVal, math.min(andToZero, 1 + orToZero), math.min(andToOne, 1 + orToOne))
      } else {
        val orVal = leftVal | rightVal
        val orToZero = leftToZero + rightToZero
        val orToOne = math.min(leftToOne, math.min(leftToZero + rightToOne, rightToZero + leftToOne))
        val andToZero = math.min(leftToZero, leftToOne + rightToZero)
        val andToOne = leftToOne + rightToOne
        Array(orVal, math.min(orToZero, 1 + andToZero), math.min(orToOne, 1 + andToOne))
      }
    }

    var index = 0

    def parseFactor(): Array[Int] = {
      if (expression(index) == '0' || expression(index) == '1') {
        val value = expression(index) - '0'
        index += 1
        Array(value, if (value == 0) 0 else 1, if (value == 0) 1 else 0)
      } else {
        index += 1
        val node = parseExpr()
        index += 1
        node
      }
    }

    def parseExpr(): Array[Int] = {
      var node = parseFactor()
      while (index < expression.length && (expression(index) == '&' || expression(index) == '|')) {
        val op = expression(index)
        index += 1
        node = combine(node, op, parseFactor())
      }
      node
    }

    val Array(value, toZero, toOne) = parseExpr()
    if (value == 0) toOne else toZero
  }
}
