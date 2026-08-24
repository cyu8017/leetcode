// LeetCode 2219 - Maximum Sum Score of Array
// https://leetcode.com/problems/maximum-sum-score-of-array/

object Solution {
  def maximumSumScore(nums: Array[Int]): Long = {
    var total = 0L
    for (x <- nums) total += x
    var pref = 0L
    var ans = Long.MinValue
    for (x <- nums) {
      pref += x
      ans = math.max(ans, math.max(pref, total - pref + x))
    }
    ans
  }
}
