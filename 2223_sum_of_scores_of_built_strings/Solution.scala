// LeetCode 2223 - Sum of Scores of Built Strings
// https://leetcode.com/problems/sum-of-scores-of-built-strings/

object Solution {
  def sumScores(s: String): Long = {
    val n = s.length
    val z = new Array[Int](n)
    var l = 0
    var r = 0
    var i = 1
    while (i < n) {
      if (i <= r) z(i) = math.min(r - i + 1, z(i - l))
      while (i + z(i) < n && s.charAt(z(i)) == s.charAt(i + z(i))) z(i) += 1
      if (i + z(i) - 1 > r) {
        l = i
        r = i + z(i) - 1
      }
      i += 1
    }
    var ans = n.toLong
    i = 1
    while (i < n) {
      ans += z(i)
      i += 1
    }
    ans
  }
}
