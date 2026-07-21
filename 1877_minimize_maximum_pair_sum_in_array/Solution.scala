// LeetCode 1877 - Minimize Maximum Pair Sum in Array
// https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

object Solution {
  def minPairSum(nums: Array[Int]): Int = {
    val sorted = nums.sorted
    var best = 0
    for (i <- 0 until sorted.length / 2) {
      best = math.max(best, sorted(i) + sorted(sorted.length - 1 - i))
    }
    best
  }
}
