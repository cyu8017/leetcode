// LeetCode 3234 - Count the Number of Substrings With Dominant Ones
// https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/

object Solution {
  def numberOfSubstrings(s: String): Int = {
    val n = s.length
    val nxt = new Array[Int](n + 1)
    nxt(n) = n
    var i = n - 1
    while (i >= 0) {
      nxt(i) = nxt(i + 1)
      if (s.charAt(i) == '0') nxt(i) = i
      i -= 1
    }
    var ans = 0
    i = 0
    while (i < n) {
      var cnt0 = if (s.charAt(i) == '0') 1 else 0
      var j = i
      while (j < n && cnt0.toLong * cnt0 <= n) {
        val cnt1 = nxt(j + 1) - i - cnt0
        if (cnt1 >= cnt0 * cnt0) {
          ans += math.min(nxt(j + 1) - j, cnt1 - cnt0 * cnt0 + 1)
        }
        j = nxt(j + 1)
        cnt0 += 1
      }
      i += 1
    }
    ans
  }
}
