// LeetCode 3305 - Count of Substrings Containing Every Vowel and K Consonants I
// https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/

object Solution {
  private def isVowel(c: Char): Boolean =
    c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'

  private def atLeast(word: String, k: Int): Int = {
    val cnt = scala.collection.mutable.HashMap.empty[Char, Int]
    var cons = 0
    var l = 0
    var ans = 0
    var r = 0
    while (r < word.length) {
      val c = word.charAt(r)
      if (isVowel(c)) cnt(c) = cnt.getOrElse(c, 0) + 1
      else cons += 1
      while (cnt.size == 5 && cons >= k) {
        ans += word.length - r
        val c2 = word.charAt(l)
        if (isVowel(c2)) {
          val nv = cnt(c2) - 1
          if (nv == 0) cnt.remove(c2)
          else cnt(c2) = nv
        } else cons -= 1
        l += 1
      }
      r += 1
    }
    ans
  }

  def countOfSubstrings(word: String, k: Int): Int = atLeast(word, k) - atLeast(word, k + 1)
}
