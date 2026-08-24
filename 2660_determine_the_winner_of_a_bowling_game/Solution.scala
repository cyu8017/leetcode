// LeetCode 2660 - Determine the Winner of a Bowling Game
// https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

object Solution {
  def isWinner(player1: Array[Int], player2: Array[Int]): Int = {
    val a = score(player1)
    val b = score(player2)
    if (a > b) 1
    else if (b > a) 2
    else 0
  }

  private def score(p: Array[Int]): Int = {
    var s = 0
    var i = 0
    while (i < p.length) {
      var mul = 1
      if ((i > 0 && p(i - 1) == 10) || (i > 1 && p(i - 2) == 10)) mul = 2
      s += mul * p(i)
      i += 1
    }
    s
  }
}
