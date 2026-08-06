// LeetCode 1946 - Largest Number After Mutating Substring
// https://leetcode.com/problems/largest-number-after-mutating-substring/

object Solution {
  def maximumNumber(num: String, change: Array[Int]): String = {
    val chars = num.toCharArray
    var started = false
    var i = 0
    while (i < chars.length) {
      val d = chars(i) - '0'
      val mapped = change(d)
      if (mapped > d) {
        chars(i) = ('0' + mapped).toChar
        started = true
      } else if (mapped < d && started) {
        return new String(chars)
      }
      i += 1
    }
    new String(chars)
  }
}
