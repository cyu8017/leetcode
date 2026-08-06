// LeetCode 1576 - Replace All ?'s to Avoid Consecutive Repeating Characters
// https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

object Solution {
  def modifyString(s: String): String = {
    val chars = s.toCharArray
    for (i <- chars.indices if chars(i) == '?') {
      chars(i) = "abc".find(c => (i == 0 || chars(i - 1) != c) && (i + 1 == chars.length || chars(i + 1) != c)).get
    }
    new String(chars)
  }
}
