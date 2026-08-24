// LeetCode 2167 - Minimum Time to Remove All Cars Containing Illegal Goods
// https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/

object Solution {
  def minimumTime(s: String): Int = {
    val n = s.length
    val left = Array.fill(n)(0)
    if (s.charAt(0) == '1') left(0) = 1
    var i = 1
    while (i < n) {
      left(i) = left(i - 1)
      if (s.charAt(i) == '1') left(i) = math.min(i + 1, left(i - 1) + 2)
      i += 1
    }
    var ans = left(n - 1)
    var right = 0
    i = n - 1
    while (i >= 0) {
      if (s.charAt(i) == '1') right = math.min(n - i, right + 2)
      val leftCost = if (i > 0) left(i - 1) else 0
      ans = math.min(ans, leftCost + right)
      i -= 1
    }
    ans
  }
}
