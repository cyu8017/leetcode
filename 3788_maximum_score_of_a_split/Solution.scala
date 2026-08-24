// LeetCode 3788 - Maximum Score Of A Split
// https://leetcode.com/problems/maximum-score-of-a-split/

object Solution {
  def maximumScore(nums: Array[Int]): Long = {
    val n = nums.length
    val suf = new Array[Long](n)
    suf(n - 1) = nums(n - 1)
    var i = n - 2
    while (i >= 0) {
      suf(i) = math.min(nums(i), suf(i + 1))
      i -= 1
    }
    var pre = 0L
    var ans = Long.MinValue
    i = 0
    while (i < n - 1) {
      pre += nums(i)
      ans = math.max(ans, pre - suf(i + 1))
      i += 1
    }
    ans
  }
}
