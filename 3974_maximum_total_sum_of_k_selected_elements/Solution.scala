// LeetCode 3974 - Maximum Total Sum of K Selected Elements
// https://leetcode.com/problems/maximum-total-sum-of-k-selected-elements/

object Solution {
  def maxSum(nums: Array[Int], k: Int, mul: Int): Long = {
    java.util.Arrays.sort(nums)
    val n = nums.length
    var ans = 0L
    var mleft = mul
    var i = n - 1
    while (i >= n - k) {
      val m = math.max(1, mleft)
      ans += nums(i).toLong * m
      mleft -= 1
      i -= 1
    }
    ans
  }
}
