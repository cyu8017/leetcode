// LeetCode 1004 - Max Consecutive Ones III
// https://leetcode.com/problems/max-consecutive-ones-iii/

object Solution {
  def longestOnes(nums: Array[Int], k: Int): Int = {
    var left = 0
    var zeros = 0
    var ans = 0
    for (right <- nums.indices) {
      if (nums(right) == 0) zeros += 1
      while (zeros > k) {
        if (nums(left) == 0) zeros -= 1
        left += 1
      }
      ans = math.max(ans, right - left + 1)
    }
    ans
  }
}
