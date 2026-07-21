// LeetCode 1823 - Find the Winner of the Circular Game
// https://leetcode.com/problems/find-the-winner-of-the-circular-game/

object Solution {
  def findTheWinner(n: Int, k: Int): Int = {
    var pos = 0
    for (size <- 2 to n) pos = (pos + k) % size
    pos + 1
  }
}
