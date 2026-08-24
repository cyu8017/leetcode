// LeetCode 2256 - Minimum Average Difference
// https://leetcode.com/problems/minimum-average-difference/

object Solution {
  def minimumAverageDifference(nums: Array[Int]): Int = {
    val n = nums.length
    var total = 0L
    for (v <- nums) total += v
    var left = 0L
    var bestDiff = Long.MaxValue
    var bestIdx = 0
    var i = 0
    while (i < n) {
      left += nums(i)
      val leftAvg = left / (i + 1)
      var rightAvg = 0L
      if (i != n - 1) rightAvg = (total - left) / (n - i - 1)
      val diff = math.abs(leftAvg - rightAvg)
      if (diff < bestDiff) {
        bestDiff = diff
        bestIdx = i
      }
      i += 1
    }
    bestIdx
  }
}
