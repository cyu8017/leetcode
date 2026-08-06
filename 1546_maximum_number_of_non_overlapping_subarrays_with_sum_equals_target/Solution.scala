// LeetCode 1546 - Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
// https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/

object Solution {
  def maxNonOverlapping(nums: Array[Int], target: Int): Int = {
    var seen = Set(0)
    var prefix = 0
    var answer = 0
    for (value <- nums) {
      prefix += value
      if (seen.contains(prefix - target)) {
        answer += 1
        prefix = 0
        seen = Set(0)
      } else seen += prefix
    }
    answer
  }
}
