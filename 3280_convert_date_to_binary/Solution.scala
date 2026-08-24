// LeetCode 3280 - Convert Date to Binary
// https://leetcode.com/problems/convert-date-to-binary/

object Solution {
  def convertDateToBinary(date: String): String = {
    val parts = date.split("-")
    val y = Integer.parseInt(parts(0))
    val m = Integer.parseInt(parts(1))
    val d = Integer.parseInt(parts(2))
    toBinary(y) + "-" + toBinary(m) + "-" + toBinary(d)
  }

  def toBinary(v0: Int): String = {
    if (v0 == 0) return "0"
    var v = v0
    val s = new StringBuilder
    while (v > 0) {
      s.insert(0, ('0' + (v & 1)).toChar)
      v >>= 1
    }
    s.toString
  }
}
