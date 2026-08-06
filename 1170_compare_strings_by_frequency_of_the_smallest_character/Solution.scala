// LeetCode 1170 - Compare Strings by Frequency of the Smallest Character
// https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

object Solution {
  def numSmallerByFrequency(queries: Array[String], words: Array[String]): Array[Int] = {
    def f(s: String): Int = s.count(_ == s.min)
    val freqs = words.map(f).sorted
    queries.map { q =>
      val fq = f(q)
      var lo = 0
      var hi = freqs.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (freqs(mid) <= fq) lo = mid + 1 else hi = mid
      }
      freqs.length - lo
    }
  }
}
