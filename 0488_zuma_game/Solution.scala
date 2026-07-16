// LeetCode 0488 - Zuma Game
// https://leetcode.com/problems/zuma-game/

import scala.collection.mutable

object Solution {
  private val memo = mutable.Map.empty[String, Int]

  def findMinStep(board: String, hand: String): Int = {
    val result = dfs(board, hand)
    if (result == Int.MaxValue) -1 else result
  }

  private def dfs(board: String, hand: String): Int = {
    val key = s"$board|$hand"
    if (memo.contains(key)) return memo(key)
    val shrunk = shrink(board)
    if (shrunk.isEmpty) {
      memo(key) = 0
      return 0
    }
    var best = Int.MaxValue
    for (i <- 0 to shrunk.length; j <- hand.indices) {
      val color = hand(j)
      val valid = (i < shrunk.length && shrunk(i) == color) || (i > 0 && shrunk(i - 1) == color)
      if (valid) {
        val newBoard = shrink(shrunk.substring(0, i) + color + shrunk.substring(i))
        if (newBoard != shrunk) {
          val newHand = hand.substring(0, j) + hand.substring(j + 1)
          val steps = dfs(newBoard, newHand)
          if (steps != Int.MaxValue) best = math.min(best, steps + 1)
        }
      }
    }
    memo(key) = best
    best
  }

  private def shrink(s: String): String = {
    var i = 0
    while (i < s.length) {
      var j = i
      while (j < s.length && s(j) == s(i)) j += 1
      if (j - i >= 3) return shrink(s.substring(0, i) + s.substring(j))
      i = j
    }
    s
  }
}
