// LeetCode 2124 - Check if All A's Appears Before All B's
// https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

object Solution {
  def checkString(s: String): Boolean = {
    var seenB = false
    var i = 0
    while (i < s.length) {
      val c = s.charAt(i)
      if (c == 'b') seenB = true
      else if (seenB) return false
      i += 1
    }
    true
  }
}
