// LeetCode 0640 - Solve the Equation
// https://leetcode.com/problems/solve-the-equation/

object Solution {
  def solveEquation(equation: String): String = {
    val eq = equation.indexOf('=')
    val left = parse(equation.substring(0, eq))
    val right = parse(equation.substring(eq + 1))
    val coef = left(0) - right(0)
    val constant = right(1) - left(1)
    if (coef == 0) return if (constant == 0) "Infinite solutions" else "No solution"
    "x=" + (constant / coef)
  }

  private def parse(expr: String): Array[Int] = {
    var coef = 0
    var constant = 0
    val n = expr.length
    var i = 0
    while (i < n) {
      var sign = 1
      if (expr.charAt(i) == '+' || expr.charAt(i) == '-') {
        sign = if (expr.charAt(i) == '-') -1 else 1
        i += 1
      }
      var value = 0
      var hasDigit = false
      while (i < n && expr.charAt(i).isDigit) {
        hasDigit = true
        value = value * 10 + (expr.charAt(i) - '0')
        i += 1
      }
      if (i < n && expr.charAt(i) == 'x') {
        coef += sign * (if (hasDigit) value else 1)
        i += 1
      } else {
        constant += sign * value
      }
    }
    Array(coef, constant)
  }
}
