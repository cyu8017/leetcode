// LeetCode 0628 - Maximum Product of Three Numbers
// https://leetcode.com/problems/maximum-product-of-three-numbers/

object Solution {
  def maximumProduct(nums: Array[Int]): Int = {
    scala.util.Sorting.quickSort(nums)
    val n = nums.length
    math.max(nums(n - 1) * nums(n - 2) * nums(n - 3), nums(0) * nums(1) * nums(n - 1))
  }
}
