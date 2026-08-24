// LeetCode 2012 - Sum of Beauty in the Array
// https://leetcode.com/problems/sum-of-beauty-in-the-array/

object Solution {
  def sumOfBeauties(nums: Array[Int]): Int = {
    val n = nums.length
    val prefixMax = Array.ofDim[Int](n)
    val suffixMin = Array.ofDim[Int](n)
    prefixMax(0) = nums(0)
    var i = 1
    while (i < n) {
      prefixMax(i) = math.max(prefixMax(i - 1), nums(i))
      i += 1
    }
    suffixMin(n - 1) = nums(n - 1)
    i = n - 2
    while (i >= 0) {
      suffixMin(i) = math.min(suffixMin(i + 1), nums(i))
      i -= 1
    }
    var ans = 0
    i = 1
    while (i < n - 1) {
      if (prefixMax(i - 1) < nums(i) && nums(i) < suffixMin(i + 1)) ans += 2
      else if (nums(i - 1) < nums(i) && nums(i) < nums(i + 1)) ans += 1
      i += 1
    }
    ans
  }
}
