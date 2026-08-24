// LeetCode 0561 - Array Partition
// https://leetcode.com/problems/array-partition/

object Solution {
  def arrayPairSum(nums: Array[Int]): Int = {
    val sorted = nums.sorted
    var total = 0
    var i = 0
    while (i < sorted.length) {
      total += sorted(i)
      i += 2
    }
    total
  }
}
