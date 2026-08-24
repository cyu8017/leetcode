// LeetCode 0644 - Maximum Average Subarray II
// https://leetcode.com/problems/maximum-average-subarray-ii/

object Solution {
  def findMaxAverage(nums: Array[Int], k: Int): Double = {
    var left = nums(0).toDouble
    var right = nums(0).toDouble
    nums.foreach { num =>
      left = math.min(left, num.toDouble)
      right = math.max(right, num.toDouble)
    }
    var i = 0
    while (i < 80) {
      val mid = (left + right) / 2.0
      if (canReach(nums, k, mid)) left = mid else right = mid
      i += 1
    }
    left
  }

  private def canReach(nums: Array[Int], k: Int, mid: Double): Boolean = {
    var prefix = 0.0
    var i = 0
    while (i < k) { prefix += nums(i) - mid; i += 1 }
    if (prefix >= 0) return true
    var prev = 0.0
    var minPrev = 0.0
    i = k
    while (i < nums.length) {
      prefix += nums(i) - mid
      prev += nums(i - k) - mid
      minPrev = math.min(minPrev, prev)
      if (prefix - minPrev >= 0) return true
      i += 1
    }
    false
  }
}
