// LeetCode 2644 - Find the Maximum Divisibility Score
// https://leetcode.com/problems/find-the-maximum-divisibility-score/

object Solution {
  def maxDivScore(nums: Array[Int], divisors: Array[Int]): Int = {
    var best = divisors(0)
    var bestScore = -1
    var i = 0
    while (i < divisors.length) {
      val d = divisors(i)
      var score = 0
      var j = 0
      while (j < nums.length) {
        if (nums(j) % d == 0) score += 1
        j += 1
      }
      if (score > bestScore || (score == bestScore && d < best)) {
        bestScore = score
        best = d
      }
      i += 1
    }
    best
  }
}
