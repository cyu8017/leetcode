// LeetCode 3255 - Find the Power of K-Size Subarrays II
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

object Solution {
  def resultsArray(nums: Array[Int], k: Int): Array[Int] = {
    val n = nums.length
    val ans = new Array[Int](n - k + 1)
    if (k == 1) return nums
    var streak = 1
    var i = 1
    while (i < n) {
      if (nums(i) == nums(i - 1) + 1) streak += 1 else streak = 1
      if (i >= k - 1) ans(i - k + 1) = if (streak >= k) nums(i) else -1
      i += 1
    }
    ans
  }
}
