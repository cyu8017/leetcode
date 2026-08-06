// LeetCode 1547 - Minimum Cost to Cut a Stick
// https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

object Solution {
  def minCost(n: Int, cuts: Array[Int]): Int = {
    val points = (0 +: cuts.sorted :+ n)
    val size = points.length
    val dp = Array.fill(size, size)(0)
    for (width <- 2 until size; left <- 0 to size - width) {
      val right = left + width
      var best = Int.MaxValue
      for (mid <- left + 1 until right) best = math.min(best, dp(left)(mid) + dp(mid)(right))
      dp(left)(right) = if (right > left + 1) best + points(right) - points(left) else 0
    }
    dp(0)(size - 1)
  }
}
