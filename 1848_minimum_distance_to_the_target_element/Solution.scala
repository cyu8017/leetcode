// LeetCode 1848 - Minimum Distance to the Target Element
// https://leetcode.com/problems/minimum-distance-to-the-target-element/

object Solution {
  def getMinDistance(nums: Array[Int], target: Int, start: Int): Int = {
    var best = nums.length
    for (i <- nums.indices if nums(i) == target) {
      best = math.min(best, math.abs(i - start))
    }
    best
  }
}
