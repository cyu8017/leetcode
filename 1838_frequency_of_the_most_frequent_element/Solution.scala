// LeetCode 1838 - Frequency of the Most Frequent Element
// https://leetcode.com/problems/frequency-of-the-most-frequent-element/

object Solution {
  def maxFrequency(nums: Array[Int], k: Int): Int = {
    val sorted = nums.sorted
    var left = 0
    var windowSum = 0L
    var best = 0
    for (right <- sorted.indices) {
      val value = sorted(right).toLong
      windowSum += value
      while (value * (right - left + 1) - windowSum > k) {
        windowSum -= sorted(left)
        left += 1
      }
      best = math.max(best, right - left + 1)
    }
    best
  }
}
