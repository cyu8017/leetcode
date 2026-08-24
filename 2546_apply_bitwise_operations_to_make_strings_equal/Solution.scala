// LeetCode 2546 - Apply Bitwise Operations to Make Strings Equal
// https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

object Solution {
  def makeStringsEqual(s: String, target: String): Boolean = {
    var has1s = false
    var has1t = false
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) == '1') has1s = true
      if (target.charAt(i) == '1') has1t = true
      i += 1
    }
    has1s == has1t
  }
}
