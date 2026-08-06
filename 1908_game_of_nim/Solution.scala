// LeetCode 1908 - Game of Nim
// https://leetcode.com/problems/game-of-nim/

object Solution {
  def nimGame(piles: Array[Int]): Boolean =
    piles.foldLeft(0)(_ ^ _) != 0
}
