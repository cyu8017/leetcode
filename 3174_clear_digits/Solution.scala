// LeetCode 3174 - Clear Digits
// https://leetcode.com/problems/clear-digits/

object Solution {
  def clearDigits(s: String): String = {
    val stk = new StringBuilder
    var i = 0
    while (i < s.length) {
      val c = s.charAt(i)
      if (c >= '0' && c <= '9') stk.deleteCharAt(stk.length - 1)
      else stk.append(c)
      i += 1
    }
    stk.toString
  }
}
