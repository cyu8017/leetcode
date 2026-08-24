// LeetCode 2278 - Percentage of Letter in String
// https://leetcode.com/problems/percentage-of-letter-in-string/

object Solution {
  def percentageLetter(s: String, letter: Char): Int = {
    var cnt = 0
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) == letter) cnt += 1
      i += 1
    }
    cnt * 100 / s.length
  }
}
