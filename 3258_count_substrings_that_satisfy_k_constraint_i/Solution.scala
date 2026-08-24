// LeetCode 3258 - Count Substrings That Satisfy K-Constraint I
// https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/

object Solution {
  def countKConstraintSubstrings(s: String, k: Int): Int = {
    var ans = 0
    val n = s.length
    var i = 0
    while (i < n) {
      var z = 0
      var o = 0
      var j = i
      var cont = true
      while (j < n && cont) {
        if (s.charAt(j) == '0') z += 1 else o += 1
        if (z <= k || o <= k) ans += 1 else cont = false
        j += 1
      }
      i += 1
    }
    ans
  }
}
