// LeetCode 1535 - Find the Winner of an Array Game
// https://leetcode.com/problems/find-the-winner-of-an-array-game/

object Solution {
  def getWinner(arr: Array[Int], k: Int): Int = {
    var champion = arr(0)
    var wins = 0
    for (i <- 1 until arr.length if wins < k) {
      if (champion > arr(i)) wins += 1
      else {
        champion = arr(i)
        wins = 1
      }
    }
    champion
  }
}
