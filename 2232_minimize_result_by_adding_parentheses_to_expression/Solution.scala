// LeetCode 2232 - Minimize Result by Adding Parentheses to Expression
// https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

object Solution {
  def minimizeResult(expression: String): String = {
    val plus = expression.indexOf('+')
    val left = expression.substring(0, plus)
    val right = expression.substring(plus + 1)
    var bestVal = Int.MaxValue
    var best = ""
    var i = 0
    while (i < left.length) {
      var j = 1
      while (j <= right.length) {
        val a = left.substring(0, i)
        val b = left.substring(i)
        val c = right.substring(0, j)
        val d = right.substring(j)
        var value = b.toInt + c.toInt
        if (a.length > 0) value *= a.toInt
        if (d.length > 0) value *= d.toInt
        val cand = a + "(" + b + "+" + c + ")" + d
        if (value < bestVal) {
          bestVal = value
          best = cand
        }
        j += 1
      }
      i += 1
    }
    best
  }
}
