// LeetCode 0070 - Climbing Stairs
// https://leetcode.com/problems/climbing-stairs/

object Solution {
  def climbStairs(n: Int): Int = {
    if (n <= 2) {
      return n
    }

    var prev = 1
    var curr = 2

    for (_ <- 3 to n) {
      val next = prev + curr
      prev = curr
      curr = next
    }

    curr
  }
}
