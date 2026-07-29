// LeetCode 1014 - Best Sightseeing Pair
// https://leetcode.com/problems/best-sightseeing-pair/

object Solution {
  def maxScoreSightseeingPair(values: Array[Int]): Int = {
    var best = values(0)
    var ans = 0
    for (j <- 1 until values.length) {
      ans = math.max(ans, best + values(j) - j)
      best = math.max(best, values(j) + j)
    }
    ans
  }
}
