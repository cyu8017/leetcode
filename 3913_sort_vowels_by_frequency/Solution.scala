// LeetCode 3913 - Sort Vowels By Frequency
// https://leetcode.com/problems/sort-vowels-by-frequency/

object Solution {
  def sortVowels(s: String): String = {
    val st = Set('a', 'e', 'i', 'o', 'u')
    val vowels = scala.collection.mutable.ArrayBuffer.empty[Char]
    val cnt = scala.collection.mutable.Map.empty[Char, Int]
    s.foreach { c =>
      if (st.contains(c)) {
        if (!cnt.contains(c)) { vowels += c; cnt(c) = 0 }
        cnt(c) = cnt(c) + 1
      }
    }
    val sortedVowels = vowels.sortBy(c => -cnt(c))
    val ans = s.toCharArray
    var i = 0
    var k = 0
    while (k < s.length) {
      if (st.contains(s.charAt(k))) {
        val ch = sortedVowels(i)
        ans(k) = ch
        cnt(ch) = cnt(ch) - 1
        if (cnt(ch) == 0) i += 1
      }
      k += 1
    }
    new String(ans)
  }
}
