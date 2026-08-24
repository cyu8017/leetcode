// LeetCode 2796 - Repeat String
// https://leetcode.com/problems/repeat-string/

object Solution {
  def replicate(str: String, times: Int): String = {
    if (times <= 0) return ""
    val sb = new StringBuilder(str.length * times)
    var i = 0
    while (i < times) {
      sb.append(str)
      i += 1
    }
    sb.toString
  }
}
