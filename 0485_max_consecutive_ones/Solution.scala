// LeetCode 0485 - Max Consecutive Ones
// https://leetcode.com/problems/max-consecutive-ones/

object Solution {
  def findMaxConsecutiveOnes(nums: Array[Int]): Int = {
    var best = 0
    var current = 0
    nums.foreach { num =>
      if (num == 1) {
        current += 1
        best = math.max(best, current)
      } else {
        current = 0
      }
    }
    best
  }
}
