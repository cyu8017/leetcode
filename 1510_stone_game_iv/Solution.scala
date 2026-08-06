// LeetCode 1510 - Stone Game IV
// https://leetcode.com/problems/stone-game-iv/

object Solution {
  def winnerSquareGame(n: Int): Boolean = {
    val win = Array.fill(n + 1)(false)
    for (value <- 1 to n) {
      var root = 1
      var can = false
      while (root * root <= value && !can) {
        if (!win(value - root * root)) can = true
        root += 1
      }
      win(value) = can
    }
    win(n)
  }
}
