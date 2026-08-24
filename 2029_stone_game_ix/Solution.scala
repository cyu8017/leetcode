// LeetCode 2029 - Stone Game IX
// https://leetcode.com/problems/stone-game-ix/

object Solution {
  def stoneGameIX(stones: Array[Int]): Boolean = {
    val cnt = Array.ofDim[Int](3)
    stones.foreach { s => cnt(s % 3) += 1 }
    if (cnt(0) % 2 == 0) cnt(1) > 0 && cnt(2) > 0
    else math.abs(cnt(1) - cnt(2)) > 2
  }
}
