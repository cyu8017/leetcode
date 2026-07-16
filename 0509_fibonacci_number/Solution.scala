// LeetCode 0509 - Fibonacci Number
// https://leetcode.com/problems/fibonacci-number/

object Solution {
  def fib(n: Int): Int = {
    if (n <= 1) return n
    var previous = 0
    var current = 1
    for (_ <- 2 to n) {
      val next = previous + current
      previous = current
      current = next
    }
    current
  }
}
