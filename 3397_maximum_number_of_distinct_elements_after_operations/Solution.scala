// LeetCode 3397 - Maximum Number of Distinct Elements After Operations
// https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

object Solution {
  def maxDistinctElements(nums: Array[Int], k: Int): Int = {
    java.util.Arrays.sort(nums)
    var ans = 0
    var prev = Long.MinValue / 2
    nums.foreach { x =>
      var cur = x.toLong - k
      if (cur <= prev) cur = prev + 1
      if (cur <= x.toLong + k) {
        ans += 1
        prev = cur
      }
    }
    ans
  }
}
