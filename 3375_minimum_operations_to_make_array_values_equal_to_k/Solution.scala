// LeetCode 3375 - Minimum Operations to Make Array Values Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/

object Solution {
  def minOperations(nums: Array[Int], k: Int): Int = {
    val seen = scala.collection.mutable.HashSet.empty[Int]
    for (x <- nums) {
      if (x < k) return -1
      if (x > k) seen += x
    }
    seen.size
  }
}
