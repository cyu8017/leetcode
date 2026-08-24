// LeetCode 2067 - Number of Equal Count Substrings
// https://leetcode.com/problems/number-of-equal-count-substrings/

object Solution {
  def equalCountSubstrings(s: String, count: Int): Int = {
    var ans = 0
    val n = s.length
    val seen = Array.ofDim[Boolean](26)
    var maxUnique = 0
    s.foreach { c =>
      if (!seen(c - 'a')) { seen(c - 'a') = true; maxUnique += 1 }
    }
    var u = 1
    while (u <= maxUnique) {
      val needLen = u * count
      if (needLen > n) { u = maxUnique + 1 }
      else {
        val freq = Array.ofDim[Int](26)
        var have = 0
        var i = 0
        while (i < n) {
          val c = s.charAt(i) - 'a'
          freq(c) += 1
          if (freq(c) == count) have += 1
          else if (freq(c) == count + 1) have -= 1
          if (i >= needLen) {
            val p = s.charAt(i - needLen) - 'a'
            if (freq(p) == count) have -= 1
            else if (freq(p) == count + 1) have += 1
            freq(p) -= 1
          }
          if (i + 1 >= needLen && have == u) ans += 1
          i += 1
        }
        u += 1
      }
    }
    ans
  }
}
