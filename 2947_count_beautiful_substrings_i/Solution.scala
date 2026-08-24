// LeetCode 2947 - Count Beautiful Substrings I
// https://leetcode.com/problems/count-beautiful-substrings-i/

object Solution {
  private def isVowel(c: Char): Boolean =
    c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'

  def beautifulSubstrings(s: String, k: Int): Int = {
    var ans = 0
    val n = s.length
    var i = 0
    while (i < n) {
      var v = 0
      var c = 0
      var j = i
      while (j < n) {
        if (isVowel(s.charAt(j))) v += 1 else c += 1
        if (v == c && (v * c) % k == 0) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
