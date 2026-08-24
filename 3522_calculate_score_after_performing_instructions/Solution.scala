// LeetCode 3522 - Calculate Score After Performing Instructions
// https://leetcode.com/problems/calculate-score-after-performing-instructions/

object Solution {
  def calculateScore(instructions: Array[String], values: Array[Int]): Long = {
    val n = values.length
    val vis = new Array[Boolean](n)
    var ans = 0L
    var i = 0
    while (i >= 0 && i < n && !vis(i)) {
      vis(i) = true
      if (instructions(i).charAt(0) == 'a') {
        ans += values(i)
        i += 1
      } else {
        i += values(i)
      }
    }
    ans
  }
}
