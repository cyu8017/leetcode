// LeetCode 3019 - Number of Changing Keys
// https://leetcode.com/problems/number-of-changing-keys/

object Solution {
  def countKeyChanges(s0: String): Int = {
    val s = s0.toLowerCase
    var ans = 0
    var i = 1
    while (i < s.length) {
      if (s.charAt(i) != s.charAt(i - 1)) ans += 1
      i += 1
    }
    ans
  }
}
