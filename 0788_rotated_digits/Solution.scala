// LeetCode 0788 - Rotated Digits
// https://leetcode.com/problems/rotated-digits/

object Solution {
  def rotatedDigits(n: Int): Int = {
    var count = 0
    var num = 1
    while (num <= n) {
      val s = num.toString
      var ok = true
      var changed = false
      s.foreach { ch =>
        if (ch == '3' || ch == '4' || ch == '7') ok = false
        if (ch == '2' || ch == '5' || ch == '6' || ch == '9') changed = true
      }
      if (ok && changed) count += 1
      num += 1
    }
    count
  }
}
