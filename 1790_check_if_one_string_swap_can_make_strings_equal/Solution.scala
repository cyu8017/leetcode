// LeetCode 1790 - Check if One String Swap Can Make Strings Equal
// https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

object Solution {
  def areAlmostEqual(s1: String, s2: String): Boolean = {
    val diff = s1.indices.filter(i => s1(i) != s2(i))
    diff.isEmpty ||
      (diff.length == 2 && s1(diff(0)) == s2(diff(1)) && s1(diff(1)) == s2(diff(0)))
  }
}
