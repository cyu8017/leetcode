// LeetCode 3987 - Minimum Total Cost to Process All Elements
// https://leetcode.com/problems/minimum-total-cost-to-process-all-elements/

object Solution {
  def minimumCost(nums: Array[Int], k: Int): Int = {
    val mod = 1000000007L
    var cnt = 0L
    var cur = k.toLong
    for (x0 <- nums) {
      val x = x0.toLong
      val diff = x - cur
      if (diff > 0) {
        val m = (diff + k - 1) / k
        cur += m * k
        cnt += m
      }
      cur -= x
    }
    cnt %= mod
    ((cnt + 1) * cnt / 2 % mod).toInt
  }
}
