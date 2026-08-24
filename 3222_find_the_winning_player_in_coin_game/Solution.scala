// LeetCode 3222 - Find the Winning Player in Coin Game
// https://leetcode.com/problems/find-the-winning-player-in-coin-game/

object Solution {
  def winningPlayer(x: Int, y: Int): String = {
    val k = math.min(x / 2, y / 8)
    val xx = x - 2 * k
    val yy = y - 8 * k
    if (xx > 0 && yy >= 4) "Alice" else "Bob"
  }
}
