// LeetCode 0643 - Maximum Average Subarray I
// https://leetcode.com/problems/maximum-average-subarray-i/

object Solution {
  def findMaxAverage(nums: Array[Int], k: Int): Double = {
    var window = 0L
    var i = 0
    while (i < k) { window += nums(i); i += 1 }
    var best = window
    i = k
    while (i < nums.length) {
      window += nums(i) - nums(i - k)
      best = math.max(best, window)
      i += 1
    }
    best.toDouble / k
  }
}
