// LeetCode 1824 - Minimum Sideway Jumps
// https://leetcode.com/problems/minimum-sideway-jumps/

object Solution {
  def minSideJumps(obstacles: Array[Int]): Int = {
    val INF = Int.MaxValue / 4
    var dp = Array(1, 0, 1)
    for (obs <- obstacles) {
      val blocked = Array(obs == 1, obs == 2, obs == 3)
      val ndp = Array(INF, INF, INF)
      for (lane <- 0 until 3 if !blocked(lane)) {
        for (other <- 0 until 3 if !blocked(other) && dp(other) < INF) {
          ndp(lane) = math.min(ndp(lane), dp(other) + (if (lane != other) 1 else 0))
        }
      }
      dp = ndp
    }
    dp.min
  }
}
