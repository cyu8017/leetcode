// LeetCode 2637 - Promise Time Limit
// https://leetcode.com/problems/promise-time-limit/

object Solution {
  def timeLimit(fn: () => Int, t: Int): () => Int = {
    () => fn()
  }
}
