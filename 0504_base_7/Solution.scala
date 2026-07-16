// LeetCode 0504 - Base 7
// https://leetcode.com/problems/base-7/

object Solution {
  def convertToBase7(num: Int): String = {
    if (num == 0) return "0"
    val negative = num < 0
    var value = math.abs(num)
    val digits = scala.collection.mutable.ArrayBuffer.empty[Char]
    while (value > 0) {
      digits += ('0' + value % 7).toChar
      value /= 7
    }
    val result = digits.reverse.mkString
    if (negative) s"-$result" else result
  }
}
