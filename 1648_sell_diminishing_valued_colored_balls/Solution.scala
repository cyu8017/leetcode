// LeetCode 1648 - Sell Diminishing-Valued Colored Balls
// https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

object Solution {
  def maxProfit(inventory: Array[Int], orders: Int): Int = {
    val MOD = 1000000007L
    val inv = inventory.sorted(Ordering[Int].reverse) :+ 0
    var remain = orders.toLong
    var ans = 0L
    var i = 0
    while (i < inv.length - 1 && remain > 0) {
      val width = (i + 1).toLong
      val high = inv(i).toLong
      val low = inv(i + 1).toLong
      val balls = width * (high - low)
      val take = math.min(remain, balls)
      val full = take / width
      val rem = take % width
      val bottom = high - full
      ans += width * (high + bottom + 1) * full / 2 + rem * bottom
      remain -= take
      i += 1
    }
    (ans % MOD).toInt
  }
}
