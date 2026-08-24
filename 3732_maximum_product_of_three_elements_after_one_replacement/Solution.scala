// LeetCode 3732 - Maximum Product of Three Elements After One Replacement
// https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/

object Solution {
  def maxProduct(nums: Array[Int]): Long = {
    java.util.Arrays.sort(nums)
    val n = nums.length
    val a = nums(0).toLong
    val b = nums(1).toLong
    val c = nums(n - 2).toLong
    val d = nums(n - 1).toLong
    val x = 100000L
    math.max(math.max(a * b * x, c * d * x), -a * d * x)
  }
}
