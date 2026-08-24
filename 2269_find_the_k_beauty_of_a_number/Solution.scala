// LeetCode 2269 - Find the K-Beauty of a Number
// https://leetcode.com/problems/find-the-k-beauty-of-a-number/

object Solution {
  def divisorSubstrings(num: Int, k: Int): Int = {
    val s = num.toString
    var ans = 0
    var i = 0
    while (i + k <= s.length) {
      var sub = 0
      var j = 0
      while (j < k) {
        sub = sub * 10 + (s.charAt(i + j) - '0')
        j += 1
      }
      if (sub != 0 && num % sub == 0) ans += 1
      i += 1
    }
    ans
  }
}
