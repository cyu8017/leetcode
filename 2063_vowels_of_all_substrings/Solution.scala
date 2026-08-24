// LeetCode 2063 - Vowels of All Substrings
// https://leetcode.com/problems/vowels-of-all-substrings/

object Solution {
  def countVowels(word: String): Long = {
    def isVowel(c: Char): Boolean = c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
    val n = word.length
    var ans = 0L
    var i = 0
    while (i < n) {
      if (isVowel(word.charAt(i))) ans += (i + 1).toLong * (n - i)
      i += 1
    }
    ans
  }
}
