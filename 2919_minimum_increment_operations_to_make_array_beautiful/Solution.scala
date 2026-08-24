// LeetCode 2919 - Minimum Increment Operations to Make Array Beautiful
// https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

object Solution {
  def minIncrementOperations(nums: Array[Int], k: Int): Long = {
    var dp0 = 0L
    var dp1 = 0L
    var dp2 = 0L
    nums.foreach { v =>
      val cost = if (v < k) k - v else 0
      val nd0 = cost + math.min(dp0, math.min(dp1, dp2))
      dp0 = dp1
      dp1 = dp2
      dp2 = nd0
    }
    math.min(dp0, math.min(dp1, dp2))
  }
}
