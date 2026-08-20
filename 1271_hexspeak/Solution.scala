// LeetCode 1271 - Hexspeak
// https://leetcode.com/problems/hexspeak/

object Solution {
  def toHexspeak(num: String): String = {
    var value = num.toLong
    val digits = "0123456789ABCDEF"
    val out = new StringBuilder
    if (value == 0) return "O"
    while (value > 0) {
      val rem = (value % 16).toInt
      value /= 16
      if (rem >= 2 && rem <= 9) return "ERROR"
      out.insert(0, digits(rem))
    }
    out.toString.replace("0", "O").replace("1", "I")
  }
}
