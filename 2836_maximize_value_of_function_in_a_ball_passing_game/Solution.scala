// LeetCode 2836 - Maximize Value of Function in a Ball Passing Game
// https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/

object Solution {
  def getMaxFunctionValue(receiver: Array[Int], k: Long): Long = {
    val n = receiver.length
    val LOG = 36
    val up = Array.ofDim[Int](LOG, n)
    val sum = Array.ofDim[Long](LOG, n)
    for (i <- 0 until n) {
      up(0)(i) = receiver(i)
      sum(0)(i) = receiver(i)
    }
    for (j <- 1 until LOG) {
      for (i <- 0 until n) {
        val mid = up(j - 1)(i)
        up(j)(i) = up(j - 1)(mid)
        sum(j)(i) = sum(j - 1)(i) + sum(j - 1)(mid)
      }
    }
    var ans = 0L
    for (i <- 0 until n) {
      var cur = i
      var total = i.toLong
      var kk = k
      for (j <- 0 until LOG) {
        if ((kk & (1L << j)) != 0) {
          total += sum(j)(cur)
          cur = up(j)(cur)
        }
      }
      ans = math.max(ans, total)
    }
    ans
  }
}
