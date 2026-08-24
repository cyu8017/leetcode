// LeetCode 3961 - Maximize Sum of Device Ratings
// https://leetcode.com/problems/maximize-sum-of-device-ratings/

object Solution {
  def maxRatings(units: Array[Array[Int]]): Long = {
    val n = units(0).length
    if (n == 1) {
      var ans = 0L
      for (x <- units) ans += x(0)
      return ans
    }
    var answer = 0L
    var mn = Int.MaxValue
    var mn2 = Int.MaxValue
    for (x <- units) {
      java.util.Arrays.sort(x)
      answer += x(1)
      mn2 = math.min(mn2, x(1))
      mn = math.min(mn, x(0))
    }
    answer - (mn2 - mn)
  }
}
