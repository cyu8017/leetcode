// LeetCode 1124 - Longest Well-Performing Interval
// https://leetcode.com/problems/longest-well-performing-interval/

object Solution {
  def longestWPI(hours: Array[Int]): Int = {
    val seen = scala.collection.mutable.Map.empty[Int, Int]
    var score = 0
    var ans = 0
    for (i <- hours.indices) {
      score += (if (hours(i) > 8) 1 else -1)
      if (score > 0) ans = i + 1
      else {
        if (!seen.contains(score)) seen(score) = i
        if (seen.contains(score - 1)) ans = math.max(ans, i - seen(score - 1))
      }
    }
    ans
  }
}
