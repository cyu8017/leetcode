// LeetCode 2953 - Count Complete Substrings
// https://leetcode.com/problems/count-complete-substrings/

object Solution {
  def countCompleteSubstrings(word: String, k: Int): Int = {
    val n = word.length
    var ans = 0
    var i = 0
    while (i < n) {
      var j = i
      while (j + 1 < n && math.abs(word.charAt(j + 1) - word.charAt(j)) <= 2) j += 1
      val seg = word.substring(i, j + 1)
      val m = seg.length
      var chars = 1
      var stop = false
      while (chars <= 26 && !stop) {
        val length = chars * k
        if (length > m) stop = true
        else {
          val freq = Array.ofDim[Int](26)
          var unique = 0
          var r = 0
          while (r < m) {
            val c = seg.charAt(r) - 'a'
            freq(c) += 1
            if (freq(c) == 1) unique += 1
            if (r >= length) {
              val c2 = seg.charAt(r - length) - 'a'
              freq(c2) -= 1
              if (freq(c2) == 0) unique -= 1
            }
            if (r >= length - 1 && unique == chars) {
              var ok = true
              var fi = 0
              while (fi < 26 && ok) {
                if (freq(fi) != 0 && freq(fi) != k) ok = false
                fi += 1
              }
              if (ok) ans += 1
            }
            r += 1
          }
        }
        chars += 1
      }
      i = j + 1
    }
    ans
  }
}
