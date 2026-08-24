// LeetCode 3325 - Count Substrings With K-Frequency Characters I
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/

object Solution {
  def numberOfSubstrings(s: String, k: Int): Int = {
    val n = s.length
    var ans = 0
    var i = 0
    while (i < n) {
      val freq = new Array[Int](26)
      var j = i
      var done = false
      while (j < n && !done) {
        freq(s.charAt(j) - 'a') += 1
        var ok = false
        var f = 0
        while (f < 26) {
          if (freq(f) >= k) ok = true
          f += 1
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
