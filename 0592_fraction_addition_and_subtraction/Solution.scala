// LeetCode 0592 - Fraction Addition and Subtraction
// https://leetcode.com/problems/fraction-addition-and-subtraction/

object Solution {
  def fractionAddition(expression: String): String = {
    var numerator = 0L
    var denominator = 1L
    var i = 0
    val len = expression.length
    while (i < len) {
      var sign = 1
      if (expression.charAt(i) == '+' || expression.charAt(i) == '-') {
        if (expression.charAt(i) == '-') sign = -1
        i += 1
      }
      var a = 0L
      while (i < len && expression.charAt(i) >= '0' && expression.charAt(i) <= '9') {
        a = a * 10 + (expression.charAt(i) - '0')
        i += 1
      }
      a *= sign
      i += 1
      var b = 0L
      while (i < len && expression.charAt(i) >= '0' && expression.charAt(i) <= '9') {
        b = b * 10 + (expression.charAt(i) - '0')
        i += 1
      }
      numerator = numerator * b + a * denominator
      denominator *= b
      val g = gcd(math.abs(numerator), math.abs(denominator))
      numerator /= g
      denominator /= g
    }
    s"$numerator/$denominator"
  }

  private def gcd(a0: Long, b0: Long): Long = {
    var a = a0
    var b = b0
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }
}
