// LeetCode 1578 - Minimum Time to Make Rope Colorful
// https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

object Solution {
  def minCost(colors: String, neededTime: Array[Int]): Int = {
    var answer = 0
    var maximum = 0
    for (i <- neededTime.indices) {
      if (i > 0 && colors(i) != colors(i - 1)) maximum = 0
      answer += math.min(maximum, neededTime(i))
      maximum = math.max(maximum, neededTime(i))
    }
    answer
  }
}
