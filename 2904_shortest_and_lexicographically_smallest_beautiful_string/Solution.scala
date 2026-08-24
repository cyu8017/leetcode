// LeetCode 2904 - Shortest and Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

object Solution {
  def shortestBeautifulSubstring(s: String, k: Int): String = {
    var ans = ""
    val n = s.length
    for (i <- 0 until n) {
      var ones = 0
      var j = i
      var done = false
      while (j < n && !done) {
        if (s.charAt(j) == '1') ones += 1
        if (ones == k) {
          val cand = s.substring(i, j + 1)
          if (ans.isEmpty || cand.length < ans.length || (cand.length == ans.length && cand < ans))
            ans = cand
          done = true
        } else if (ones > k) done = true
        j += 1
      }
    }
    ans
  }
}
