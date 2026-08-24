// LeetCode 2017 - Grid Game
// https://leetcode.com/problems/grid-game/

object Solution {
  def gridGame(grid: Array[Array[Int]]): Long = {
    val n = grid(0).length
    var top = 0L
    grid(0).foreach { v => top += v }
    var bottom = 0L
    var ans = Long.MaxValue
    var i = 0
    while (i < n) {
      top -= grid(0)(i)
      ans = math.min(ans, math.max(top, bottom))
      bottom += grid(1)(i)
      i += 1
    }
    ans
  }
}
