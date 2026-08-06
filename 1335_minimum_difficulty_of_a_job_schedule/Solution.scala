// LeetCode 1335 - Minimum Difficulty of a Job Schedule
// https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

object Solution {
  def minDifficulty(jobDifficulty: Array[Int], d: Int): Int = {
    val n = jobDifficulty.length
    if (n < d) return -1
    val dp = Array.fill(n)(1000000000)
    var hardest = 0
    for (i <- 0 until n) {
      hardest = math.max(hardest, jobDifficulty(i))
      dp(i) = hardest
    }
    for (day <- 1 until d) {
      val nxt = Array.fill(n)(1000000000)
      for (end <- day until n) {
        hardest = 0
        for (start <- end to day by -1) {
          hardest = math.max(hardest, jobDifficulty(start))
          nxt(end) = math.min(nxt(end), dp(start - 1) + hardest)
        }
      }
      for (i <- 0 until n) dp(i) = nxt(i)
    }
    dp(n - 1)
  }
}
