// LeetCode 3046 - Split the Array
// https://leetcode.com/problems/split-the-array/

object Solution {
  def isPossibleToSplit(nums: Array[Int]): Boolean = {
    val cnt = Array.ofDim[Int](101)
    for (x <- nums) {
      cnt(x) += 1
      if (cnt(x) >= 3) return false
    }
    true
  }
}
