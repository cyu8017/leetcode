// LeetCode 3107 - Minimum Operations to Make Median of Array Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/

object Solution {
  def minOperationsToMakeMedianK(nums: Array[Int], k: Int): Long = {
    val a = nums.sorted
    val n = a.length
    val m = n >> 1
    var ans = math.abs(a(m) - k).toLong
    if (a(m) > k) {
      var i = m - 1
      while (i >= 0 && a(i) > k) {
        ans += a(i) - k
        i -= 1
      }
    } else {
      var i = m + 1
      while (i < n && a(i) < k) {
        ans += k - a(i)
        i += 1
      }
    }
    ans
  }
}
