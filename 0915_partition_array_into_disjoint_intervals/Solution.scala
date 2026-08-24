// LeetCode 0915 - Partition Array into Disjoint Intervals
// https://leetcode.com/problems/partition-array-into-disjoint-intervals/

object Solution {
  def partitionDisjoint(nums: Array[Int]): Int = {
    val n = nums.length
    val minRight = Array.ofDim[Int](n)
    minRight(n - 1) = nums(n - 1)
    var i = n - 2
    while (i >= 0) {
      minRight(i) = math.min(nums(i), minRight(i + 1))
      i -= 1
    }
    var maxLeft = nums(0)
    i = 1
    while (i < n) {
      if (maxLeft <= minRight(i)) return i
      maxLeft = math.max(maxLeft, nums(i))
      i += 1
    }
    n - 1
  }
}
