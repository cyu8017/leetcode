// LeetCode 3512 - Minimum Operations to Make Array Sum Divisible by K
// https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

object Solution {
  def minOperations(nums: Array[Int], k: Int): Int = {
    var ans = 0
    for (x <- nums) ans = (ans + x) % k
    ans
  }
}
