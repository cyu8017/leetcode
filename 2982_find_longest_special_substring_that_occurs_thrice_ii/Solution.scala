// LeetCode 2982 - Find Longest Special Substring That Occurs Thrice II
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/

object Solution {
  def maximumLength(s: String): Int = {
    val groups = Array.fill(26)(scala.collection.mutable.ArrayBuffer.empty[Int])
    val n = s.length
    var i = 0
    while (i < n) {
      var j = i
      while (j < n && s.charAt(j) == s.charAt(i)) j += 1
      groups(s.charAt(i) - 'a') += (j - i)
      i = j
    }
    var ans = -1
    var c = 0
    while (c < 26) {
      val arr = groups(c)
      if (arr.nonEmpty) {
        val sorted = arr.sorted(Ordering[Int].reverse)
        var L = sorted(0)
        var done = false
        while (L >= 1 && !done) {
          var cnt = 0
          for (g <- sorted) if (g >= L) cnt += g - L + 1
          if (cnt >= 3) {
            if (L > ans) ans = L
            done = true
          }
          L -= 1
        }
      }
      c += 1
    }
    ans
  }
}
