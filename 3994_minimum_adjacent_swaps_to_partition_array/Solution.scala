// LeetCode 3994 - Minimum Adjacent Swaps to Partition Array
// https://leetcode.com/problems/minimum-adjacent-swaps-to-partition-array/

object Solution {
  def minAdjacentSwaps(nums: Array[Int], a: Int, b: Int): Int = {
    val MOD = 1000000007
    var result = 0
    var cnt1 = 0
    var cnt2 = 0
    for (x <- nums) {
      if (x < a) result = (result + cnt1 + cnt2) % MOD
      else if (x <= b) {
        cnt1 += 1
        result = (result + cnt2) % MOD
      } else cnt2 += 1
    }
    result
  }
}
