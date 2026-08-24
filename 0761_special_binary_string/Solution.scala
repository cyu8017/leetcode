// LeetCode 0761 - Special Binary String
// https://leetcode.com/problems/special-binary-string/

object Solution {
  def makeLargestSpecial(s: String): String = {
    val parts = scala.collection.mutable.ArrayBuffer.empty[String]
    var balance = 0
    var start = 0
    var i = 0
    while (i < s.length) {
      balance += (if (s.charAt(i) == '1') 1 else -1)
      if (balance == 0) {
        parts += "1" + makeLargestSpecial(s.substring(start + 1, i)) + "0"
        start = i + 1
      }
      i += 1
    }
    parts.sortWith(_ > _).mkString
  }
}
