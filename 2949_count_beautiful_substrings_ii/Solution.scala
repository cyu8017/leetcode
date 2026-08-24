// LeetCode 2949 - Count Beautiful Substrings II
// https://leetcode.com/problems/count-beautiful-substrings-ii/

object Solution {
  private def isVowel(c: Char): Boolean =
    c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'

  def beautifulSubstrings(s: String, k: Int): Long = {
    var x = 1
    while ((x * x) % k != 0) x += 1
    val freq = scala.collection.mutable.HashMap[Long, Int]()
    freq(0L) = 1
    var bal = 0
    var vowels = 0
    var ans = 0L
    var i = 0
    while (i < s.length) {
      val ch = s.charAt(i)
      if (isVowel(ch)) { bal += 1; vowels += 1 } else bal -= 1
      val kk = (bal.toLong << 32) | (vowels % x)
      val f = freq.getOrElse(kk, 0)
      ans += f
      freq(kk) = f + 1
      i += 1
    }
    ans
  }
}
