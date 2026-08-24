// LeetCode 3566 - Partition Array into Two Equal Product Subsets
// https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/

object Solution {
  def checkEqualPartitions(nums: Array[Int], target: Long): Boolean = {
    val n = nums.length
    var i = 0
    while (i < (1 << n)) {
      var x = 1L
      var y = 1L
      var j = 0
      var overflow = false
      while (j < n && !overflow) {
        if (((i >> j) & 1) != 0) x *= nums(j)
        else y *= nums(j)
        if (x > target || y > target) overflow = true
        j += 1
      }
      if (x == target && y == target) return true
      i += 1
    }
    false
  }
}
