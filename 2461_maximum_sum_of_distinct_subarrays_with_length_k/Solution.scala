// LeetCode 2461 - Maximum Sum of Distinct Subarrays With Length K
// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

object Solution {
  def maximumSubarraySum(nums: Array[Int], k: Int): Long = {
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    var sum = 0L
    var ans = 0L
    var i = 0
    while (i < nums.length) {
      sum += nums(i)
      cnt(nums(i)) = cnt.getOrElse(nums(i), 0) + 1
      if (i >= k) {
        val y = nums(i - k)
        sum -= y
        val c = cnt(y) - 1
        if (c == 0) cnt.remove(y) else cnt(y) = c
      }
      if (i >= k - 1 && cnt.size == k && sum > ans) ans = sum
      i += 1
    }
    ans
  }
}
