// LeetCode 2958 - Length of Longest Subarray With at Most K Frequency
// https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

object Solution {
  def maxSubarrayLength(nums: Array[Int], k: Int): Int = {
    val freq = scala.collection.mutable.HashMap[Int, Int]()
    var ans = 0
    var left = 0
    var right = 0
    while (right < nums.length) {
      freq(nums(right)) = freq.getOrElse(nums(right), 0) + 1
      while (freq(nums(right)) > k) {
        freq(nums(left)) = freq(nums(left)) - 1
        left += 1
      }
      if (right - left + 1 > ans) ans = right - left + 1
      right += 1
    }
    ans
  }
}
