// LeetCode 2140 - Solving Questions With Brainpower
// https://leetcode.com/problems/solving-questions-with-brainpower/

object Solution {
  def mostPoints(questions: Array[Array[Int]]): Long = {
    val n = questions.length
    val dp = Array.fill(n + 1)(0L)
    var i = n - 1
    while (i >= 0) {
      val pts = questions(i)(0)
      val brain = questions(i)(1)
      val next = i + brain + 1
      val take = pts + (if (next < n) dp(next) else 0L)
      dp(i) = math.max(dp(i + 1), take)
      i -= 1
    }
    dp(0)
  }
}
