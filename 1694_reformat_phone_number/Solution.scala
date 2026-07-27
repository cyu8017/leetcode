// LeetCode 1694 - Reformat Phone Number
// https://leetcode.com/problems/reformat-phone-number/

object Solution {
  def reformatNumber(number: String): String = {
    var s = number.filter(c => c >= '0' && c <= '9')
    val out = scala.collection.mutable.ArrayBuffer[String]()
    while (s.length > 4) {
      out += s.take(3)
      s = s.drop(3)
    }
    if (s.length == 4) {
      out += s.take(2)
      out += s.drop(2)
    } else if (s.nonEmpty) {
      out += s
    }
    out.mkString("-")
  }
}
