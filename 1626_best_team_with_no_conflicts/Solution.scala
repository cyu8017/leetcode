// LeetCode 1626 - Best Team With No Conflicts
// https://leetcode.com/problems/best-team-with-no-conflicts/

object Solution {
  def bestTeamScore(scores: Array[Int], ages: Array[Int]): Int = {
    val players = ages.zip(scores).sortBy(p => (p._1, p._2))
    val dp = Array.fill(players.length)(0)
    players.indices.foreach { i =>
      val score = players(i)._2
      var best = 0
      var j = 0
      while (j < i) {
        if (players(j)._2 <= score) best = math.max(best, dp(j))
        j += 1
      }
      dp(i) = score + best
    }
    if (dp.isEmpty) 0 else dp.max
  }
}
