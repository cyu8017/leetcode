// LeetCode 3021 - Alice and Bob Playing Flower Game
// https://leetcode.com/problems/alice-and-bob-playing-flower-game/

object Solution {
  def flowerGame(n: Int, m: Int): Long = {
    val a1 = (n + 1) / 2
    val b1 = (m + 1) / 2
    val a2 = n / 2
    val b2 = m / 2
    a1.toLong * b2 + a2.toLong * b1
  }
}
