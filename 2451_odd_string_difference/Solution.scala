// LeetCode 2451 - Odd String Difference
// https://leetcode.com/problems/odd-string-difference/

object Solution {
  def oddString(words: Array[String]): String = {
    def diff(w: String): String = {
      val b = new StringBuilder()
      var i = 1
      while (i < w.length) {
        val d = w.charAt(i) - w.charAt(i - 1)
        b.append((d + 128).toChar)
        b.append(',')
        i += 1
      }
      b.toString
    }
    val d0 = diff(words(0))
    val d1 = diff(words(1))
    if (d0 == d1) {
      var i = 2
      while (i < words.length) {
        if (diff(words(i)) != d0) return words(i)
        i += 1
      }
    }
    if (diff(words(2)) == d0) words(1) else words(0)
  }
}
