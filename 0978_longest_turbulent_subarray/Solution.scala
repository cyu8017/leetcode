// LeetCode 0978 - Longest Turbulent Subarray
// https://leetcode.com/problems/longest-turbulent-subarray/

object Solution {
  def maxTurbulenceSize(arr: Array[Int]): Int = {
    var ans = 1
    var cur = 1
    var i = 1
    while (i < arr.length) {
      if (arr(i) == arr(i - 1)) cur = 1
      else if (i == 1 || (arr(i).toLong - arr(i - 1)) * (arr(i - 1).toLong - arr(i - 2)) < 0) cur += 1
      else cur = 2
      ans = math.max(ans, cur)
      i += 1
    }
    ans
  }
}
