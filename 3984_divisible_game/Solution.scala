// LeetCode 3984 - Divisible Game
// https://leetcode.com/problems/divisible-game/

import scala.collection.mutable

object Solution {
  def divisibleGame(nums: Array[Int]): Int = {
    val candidates = mutable.HashSet[Int](2)
    for (value <- nums) {
      var divisor = 2
      while (divisor * divisor <= value) {
        if (value % divisor == 0) {
          candidates += divisor
          candidates += value / divisor
        }
        divisor += 1
      }
      if (value > 1) candidates += value
    }
    var bestScore = -(1L << 62)
    var bestK = 0
    for (k <- candidates) {
      var ending = 0L
      var score = 0L
      var i = 0
      while (i < nums.length) {
        val value = nums(i)
        var contribution = -value.toLong
        if (value % k == 0) contribution = value
        if (i == 0 || ending + contribution < contribution) ending = contribution
        else ending += contribution
        if (i == 0 || ending > score) score = ending
        i += 1
      }
      if (score > bestScore || (score == bestScore && k < bestK)) {
        bestScore = score
        bestK = k
      }
    }
    val mod = 1000000007L
    var answer = (bestScore % mod) * bestK % mod
    if (answer < 0) answer += mod
    answer.toInt
  }
}
