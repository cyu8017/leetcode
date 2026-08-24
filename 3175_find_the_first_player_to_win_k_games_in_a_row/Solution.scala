// LeetCode 3175 - Find The First Player to win K Games in a Row
// https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/

object Solution {
  def findWinningPlayer(skills: Array[Int], k: Int): Int = {
    val n = skills.length
    val kk = math.min(k, n - 1)
    var i = 0
    var cnt = 0
    var j = 1
    while (j < n) {
      if (skills(i) < skills(j)) { i = j; cnt = 1 }
      else cnt += 1
      if (cnt == kk) return i
      j += 1
    }
    i
  }
}
