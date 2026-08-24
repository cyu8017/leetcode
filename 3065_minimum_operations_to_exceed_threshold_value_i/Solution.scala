// LeetCode 3065 - Minimum Operations to Exceed Threshold Value I
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

object Solution {
  def minOperations(nums: Array[Int], k: Int): Int = {
    var ans = 0
    nums.foreach { x => if (x < k) ans += 1 }
    ans
  }
}
