// LeetCode 0209 - Minimum Size Subarray Sum\n// https://leetcode.com/problems/\n\nobject Solution {
  def minSubArrayLen(target: Int, nums: Array[Int]): Int = {
    var left = 0
    var sum = 0
    var best = Int.MaxValue
    for (right <- nums.indices) {
      sum += nums(right)
      while (sum >= target) { best = math.min(best, right - left + 1); sum -= nums(left); left += 1 }
    }
    if (best == Int.MaxValue) 0 else best
  }
}
