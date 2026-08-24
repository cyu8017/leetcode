// LeetCode 2743 - Count Substrings Without Repeating Character
// https://leetcode.com/problems/count-substrings-without-repeating-character/

object Solution {
  def numberOfSpecialSubstrings(s: String): Int = {
    val n = s.length
    var ans = 0
    var left = 0
    val cnt = Array.fill(26)(0)
    var i = 0
    while (i < n) {
      val c = s.charAt(i) - 'a'
      cnt(c) += 1
      while (cnt(c) > 1) {
        cnt(s.charAt(left) - 'a') -= 1
        left += 1
      }
      ans += i - left + 1
      i += 1
    }
    ans
  }
}
