// LeetCode 0043 - Multiply Strings
// https://leetcode.com/problems/multiply-strings/

object Solution {
  def multiply(num1: String, num2: String): String = {
    if (num1 == "0" || num2 == "0") {
      return "0"
    }

    val positions = Array.fill(num1.length + num2.length)(0)

    for (i <- num1.length - 1 to 0 by -1) {
      for (j <- num2.length - 1 to 0 by -1) {
        val product = (num1(i) - '0') * (num2(j) - '0')
        val low = i + j + 1
        val high = i + j
        val total = product + positions(low)
        positions(low) = total % 10
        positions(high) += total / 10
      }
    }

    val start = positions.indexWhere(_ != 0)
    if (start == -1) {
      "0"
    } else {
      positions.drop(start).mkString
    }
  }
}
