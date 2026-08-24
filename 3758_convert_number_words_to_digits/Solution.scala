// LeetCode 3758 - Convert Number Words To Digits
// https://leetcode.com/problems/convert-number-words-to-digits/

object Solution {
  def convertNumber(s: String): String = {
    val d = Array("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    val n = s.length
    val ans = new StringBuilder
    var i = 0
    while (i < n) {
      var j = 0
      var matched = false
      while (j < 10 && !matched) {
        val m = d(j).length
        if (i + m <= n && s.substring(i, i + m) == d(j)) {
          ans.append(('0' + j).toChar)
          i += m - 1
          matched = true
        }
        j += 1
      }
      i += 1
    }
    ans.toString
  }
}
