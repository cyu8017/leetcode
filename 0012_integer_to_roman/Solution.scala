// LeetCode 0012 - Integer to Roman
// https://leetcode.com/problems/integer-to-roman/

object Solution {
  def intToRoman(num: Int): String = {
    val values = Array(1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    val symbols = Array("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
    var value = num
    val result = new StringBuilder

    for (i <- values.indices) {
      while (value >= values(i)) {
        result.append(symbols(i))
        value -= values(i)
      }
    }

    result.toString
  }
}
