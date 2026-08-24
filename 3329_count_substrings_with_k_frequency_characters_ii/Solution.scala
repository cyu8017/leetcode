// LeetCode 3329 - Count Substrings With K-Frequency Characters II
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-ii/

object Solution {
  def numberOfSubstrings(s: String, k: Int): Long = {
    val n = s.length
    var ans = 0L
    var i = 0
    while (i < n) {
      val freq = new Array[Int](26)
      var j = i
      var done = false
      while (j < n && !done) {
        freq(s.charAt(j) - 'a') += 1
        var ok = false
        var t = 0
        while (t < 26) {
          if (freq(t) >= k) ok = true
          t += 1
        }
        if (ok) {
          ans += n - j
          done = true
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
