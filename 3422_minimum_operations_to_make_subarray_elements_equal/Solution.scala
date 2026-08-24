// LeetCode 3422 - Minimum Operations to Make Subarray Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/

object Solution {
  def minOperations(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    var ans = 1L << 62
    var i = 0
    while (i + k <= n) {
      val sub = java.util.Arrays.copyOfRange(nums, i, i + k)
      java.util.Arrays.sort(sub)
      val med = sub(k / 2)
      var cost = 0L
      sub.foreach { x => cost += math.abs(x - med) }
      if (cost < ans) ans = cost
      i += 1
    }
    ans
  }
}
