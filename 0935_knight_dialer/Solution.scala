// LeetCode 0935 - Knight Dialer
// https://leetcode.com/problems/knight-dialer/

object Solution {
  def knightDialer(n: Int): Int = {
    val MOD = 1000000007
    val moves = Array(
      Array(4, 6), Array(6, 8), Array(7, 9), Array(4, 8), Array(0, 3, 9),
      Array.empty[Int], Array(0, 1, 7), Array(2, 6), Array(1, 3), Array(2, 4)
    )
    var dp = Array.fill(10)(1L)
    var step = 0
    while (step < n - 1) {
      val ndp = Array.ofDim[Long](10)
      var i = 0
      while (i < 10) {
        moves(i).foreach { j => ndp(j) = (ndp(j) + dp(i)) % MOD }
        i += 1
      }
      dp = ndp
      step += 1
    }
    (dp.sum % MOD).toInt
  }
}
