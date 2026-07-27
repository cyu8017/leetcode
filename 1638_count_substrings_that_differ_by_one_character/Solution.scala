// LeetCode 1638 - Count Substrings That Differ by One Character
// https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

object Solution {
  def countSubstrings(s: String, t: String): Int = {
    var ans = 0
    for (i <- s.indices; j <- t.indices) {
      var diff = 0
      var k = 0
      while (k < math.min(s.length - i, t.length - j)) {
        if (s.charAt(i + k) != t.charAt(j + k)) diff += 1
        if (diff == 1) ans += 1
        else if (diff > 1) { k = Int.MaxValue - 1 }
        k += 1
      }
    }
    ans
  }
}
