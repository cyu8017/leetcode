// LeetCode 2914 - Minimum Number of Changes to Make Binary String Beautiful
// https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

object Solution {
  def minChanges(s: String): Int = {
    var ans = 0
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) != s.charAt(i + 1)) ans += 1
      i += 2
    }
    ans
  }
}
