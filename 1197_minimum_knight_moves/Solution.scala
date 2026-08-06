// LeetCode 1197 - Minimum Knight Moves
// https://leetcode.com/problems/minimum-knight-moves/

object Solution {
  def minKnightMoves(x: Int, y: Int): Int = {
    val ax = math.abs(x)
    val ay = math.abs(y)
    val memo = scala.collection.mutable.Map.empty[(Int, Int), Int]
    def dfs(a: Int, b: Int): Int = {
      val (aa, bb) = if (a < b) (b, a) else (a, b)
      if (aa + bb == 0) return 0
      if (aa + bb == 2) return 2
      memo.getOrElseUpdate((aa, bb), {
        math.min(dfs(math.abs(aa - 1), math.abs(bb - 2)), dfs(math.abs(aa - 2), math.abs(bb - 1))) + 1
      })
    }
    dfs(ax, ay)
  }
}
