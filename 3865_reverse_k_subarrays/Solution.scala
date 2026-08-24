// LeetCode 3865 - Reverse K Subarrays
// https://leetcode.com/problems/reverse-k-subarrays/

object Solution {
  def reverseSubarrays(nums: Array[Int], k: Int): Array[Int] = {
    val n = nums.length
    val m = n / k
    var i = 0
    while (i < n) {
      var lo = i
      var hi = i + m - 1
      while (lo < hi) {
        val t = nums(lo)
        nums(lo) = nums(hi)
        nums(hi) = t
        lo += 1
        hi -= 1
      }
      i += m
    }
    nums
  }
}
