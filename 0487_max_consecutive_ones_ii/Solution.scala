// LeetCode 0487 - Max Consecutive Ones II
// https://leetcode.com/problems/max-consecutive-ones-ii/

object Solution {
  def findMaxConsecutiveOnes(nums: Array[Int]): Int = {
    var left = 0
    var best = 0
    var zeros = 0
    nums.indices.foreach { right =>
      if (nums(right) == 0) zeros += 1
      while (zeros > 1) {
        if (nums(left) == 0) zeros -= 1
        left += 1
      }
      best = math.max(best, right - left + 1)
    }
    best
  }
}
