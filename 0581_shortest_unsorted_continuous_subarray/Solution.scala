// LeetCode 0581 - Shortest Unsorted Continuous Subarray
// https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

object Solution {
  def findUnsortedSubarray(nums: Array[Int]): Int = {
    val n = nums.length
    var left = -1
    var right = -2
    var maxSeen = nums(0)
    var minSeen = nums(n - 1)
    var i = 0
    while (i < n) {
      maxSeen = math.max(maxSeen, nums(i))
      if (nums(i) < maxSeen) right = i
      val j = n - 1 - i
      minSeen = math.min(minSeen, nums(j))
      if (nums(j) > minSeen) left = j
      i += 1
    }
    right - left + 1
  }
}
