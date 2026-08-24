// LeetCode 0992 - Subarrays with K Different Integers
// https://leetcode.com/problems/subarrays-with-k-different-integers/

object Solution {
  def subarraysWithKDistinct(nums: Array[Int], k: Int): Int = {
    atMost(nums, k) - atMost(nums, k - 1)
  }

  private def atMost(nums: Array[Int], m: Int): Int = {
    if (m < 0) return 0
    val count = scala.collection.mutable.Map.empty[Int, Int]
    var left = 0
    var ans = 0
    var right = 0
    while (right < nums.length) {
      count(nums(right)) = count.getOrElse(nums(right), 0) + 1
      while (count.size > m) {
        val v = nums(left)
        left += 1
        count(v) = count(v) - 1
        if (count(v) == 0) count.remove(v)
      }
      ans += right - left + 1
      right += 1
    }
    ans
  }
}
