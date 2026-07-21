// LeetCode 1883 - Minimum Skips to Arrive at Meeting On Time
// https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/

object Solution {
  def minSkips(dist: Array[Int], speed: Int, hoursBefore: Int): Int = {
    val limit = hoursBefore.toLong * speed
    val n = dist.length
    val INF = Long.MaxValue / 4
    var dp = Array.fill(n + 1)(INF)
    dp(0) = 0L
    for (road <- dist) {
      val nxt = Array.fill(n + 1)(INF)
      for (skips <- 0 until n if dp(skips) < INF) {
        val ceiled = ((dp(skips) + road + speed - 1) / speed) * speed
        nxt(skips) = math.min(nxt(skips), ceiled)
        nxt(skips + 1) = math.min(nxt(skips + 1), dp(skips) + road)
      }
      dp = nxt
    }
    for (skips <- dp.indices if dp(skips) <= limit) {
      return skips
    }
    -1
  }
}
