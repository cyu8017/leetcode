// LeetCode 3487 - Maximum Unique Subarray Sum After Deletion
// https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

object Solution {
  def maxSum(nums: Array[Int]): Int = {
    val seen = scala.collection.mutable.Set.empty[Int]
    var sum = 0
    var hasPos = false
    var maxNeg = -1000000000
    nums.foreach { x =>
      if (x < 0) {
        if (x > maxNeg) maxNeg = x
      } else {
        hasPos = true
        if (seen.add(x)) sum += x
      }
    }
    if (hasPos) sum else maxNeg
  }
}
