// LeetCode 2537 - Count the Number of Good Subarrays
// https://leetcode.com/problems/count-the-number-of-good-subarrays/

object Solution {
  def countGood(nums: Array[Int], k: Int): Long = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    var pairs = 0L
    var ans = 0L
    var left = 0
    var right = 0
    while (right < nums.length) {
      pairs += freq.getOrElse(nums(right), 0)
      freq(nums(right)) = freq.getOrElse(nums(right), 0) + 1
      while (pairs >= k) {
        ans += nums.length - right
        freq(nums(left)) = freq(nums(left)) - 1
        pairs -= freq(nums(left))
        left += 1
      }
      right += 1
    }
    ans
  }
}
