// LeetCode 1759 - Count Number of Homogenous Substrings
// https://leetcode.com/problems/count-number-of-homogenous-substrings/

object Solution {
  def countHomogenous(s: String): Int = {
    val mod = 1000000007L
    var ans = 0L
    var i = 0
    while (i < s.length) {
      var j = i
      while (j < s.length && s(j) == s(i)) {
        j += 1
      }
      val length = (j - i).toLong
      ans = (ans + length * (length + 1) / 2) % mod
      i = j
    }
    ans.toInt
  }
}
