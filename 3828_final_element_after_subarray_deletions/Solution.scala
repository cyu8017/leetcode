// LeetCode 3828 - Final Element After Subarray Deletions
// https://leetcode.com/problems/final-element-after-subarray-deletions/

object Solution {
  def finalElement(nums: Array[Int]): Int = math.max(nums(0), nums(nums.length - 1))
}
