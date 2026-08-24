// LeetCode 2403 - Minimum Time to Kill All Monsters
// https://leetcode.com/problems/minimum-time-to-kill-all-monsters/

object Solution {
  def minimumTime(power: Array[Int]): Long = {
    val n = power.length
    val N = 1 << n
    val dp = Array.fill(N)(Long.MaxValue / 4)
    dp(0) = 0
    var mask = 0
    while (mask < N) {
      val killed = Integer.bitCount(mask)
      val gain = killed + 1L
      var i = 0
      while (i < n) {
        if ((mask & (1 << i)) == 0) {
          val need = (power(i) + gain - 1) / gain
          val nm = mask | (1 << i)
          dp(nm) = math.min(dp(nm), dp(mask) + need)
        }
        i += 1
      }
      mask += 1
    }
    dp(N - 1)
  }
}
