// LeetCode 2062 - Count Vowel Substrings of a String
// https://leetcode.com/problems/count-vowel-substrings-of-a-string/

object Solution {
  def countVowelSubstrings(word: String): Int = {
    def isVowel(c: Char): Boolean = c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
    var ans = 0
    val n = word.length
    var i = 0
    while (i < n) {
      val seen = scala.collection.mutable.HashSet.empty[Char]
      var j = i
      while (j < n && isVowel(word.charAt(j))) {
        seen += word.charAt(j)
        if (seen.size == 5) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
