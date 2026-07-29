// LeetCode 1040 - Moving Stones Until Consecutive II
// https://leetcode.com/problems/moving-stones-until-consecutive-ii/

object Solution {
  def numMovesStonesII(stones: Array[Int]): Array[Int] = {
    val s = stones.sorted
    val n = s.length
    val maxMoves = math.max(s(n - 1) - s(1) - n + 2, s(n - 2) - s(0) - n + 2)
    var minMoves = maxMoves
    var i = 0
    for (j <- 0 until n) {
      while (s(j) - s(i) + 1 > n) i += 1
      val inside = j - i + 1
      if (inside == n - 1 && s(j) - s(i) + 1 == n - 1) minMoves = math.min(minMoves, 2)
      else minMoves = math.min(minMoves, n - inside)
    }
    Array(minMoves, maxMoves)
  }
}
