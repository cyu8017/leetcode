// LeetCode 2090 - K Radius Subarray Averages
// https://leetcode.com/problems/k-radius-subarray-averages/

object Solution {
  def getAverages(nums: Array[Int], k: Int): Array[Int] = {
    val n = nums.length
    val ans = Array.fill(n)(-1)
    if (2 * k + 1 > n) return ans
    var sum = 0L
    var i = 0
    while (i < 2 * k + 1) {
      sum += nums(i)
      i += 1
    }
    ans(k) = (sum / (2 * k + 1)).toInt
    i = k + 1
    while (i + k < n) {
      sum += nums(i + k) - nums(i - k - 1)
      ans(i) = (sum / (2 * k + 1)).toInt
      i += 1
    }
    ans
  }
}
