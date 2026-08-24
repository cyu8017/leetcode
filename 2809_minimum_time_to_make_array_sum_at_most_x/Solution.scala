// LeetCode 2809 - Minimum Time to Make Array Sum At Most x
// https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/

object Solution {
  def minimumTime(nums1: List[Int], nums2: List[Int], x: Int): Int = {
    val n = nums1.length
    val arr = Array.tabulate(n)(i => Array(nums1(i), nums2(i)))
    var sum1 = 0
    var sum2 = 0
    var i = 0
    while (i < n) {
      sum1 += nums1(i)
      sum2 += nums2(i)
      i += 1
    }
    java.util.Arrays.sort(arr, (u: Array[Int], v: Array[Int]) => Integer.compare(u(1), v(1)))
    val dp = Array.ofDim[Int](n + 1)
    i = 0
    while (i < n) {
      var j = i + 1
      while (j >= 1) {
        dp(j) = math.max(dp(j), dp(j - 1) + arr(i)(0) + j * arr(i)(1))
        j -= 1
      }
      i += 1
    }
    var t = 0
    while (t <= n) {
      if (sum1 + sum2 * t - dp(t) <= x) return t
      t += 1
    }
    -1
  }
}
