// LeetCode 1704 - Determine if String Halves Are Alike
// https://leetcode.com/problems/determine-if-string-halves-are-alike/

object Solution {
  def halvesAreAlike(s: String): Boolean = {
    val vowels = "aeiouAEIOU".toSet
    val mid = s.length / 2
    s.take(mid).count(vowels.contains) == s.drop(mid).count(vowels.contains)
  }
}
