// LeetCode 3856 - Trim Trailing Vowels
// https://leetcode.com/problems/trim-trailing-vowels/

object Solution {
  def trimTrailingVowels(s: String): String = {
    var i = s.length - 1
    while (i >= 0 && isVowel(s.charAt(i))) i -= 1
    s.substring(0, i + 1)
  }

  private def isVowel(c: Char): Boolean =
    c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
}
