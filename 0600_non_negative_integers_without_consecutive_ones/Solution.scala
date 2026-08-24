// LeetCode 0600 - Non-negative Integers without Consecutive Ones
// https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/

object Solution {
  def findIntegers(n: Int): Int = {
    val fib = Array.fill(32)(0)
    fib(0) = 1
    fib(1) = 2
    var i = 2
    while (i < 32) { fib(i) = fib(i - 1) + fib(i - 2); i += 1 }
    var answer = 0
    var prevBit = 0
    var bit = 30
    while (bit >= 0) {
      if ((n & (1 << bit)) != 0) {
        answer += fib(bit)
        if (prevBit == 1) return answer
        prevBit = 1
      } else {
        prevBit = 0
      }
      bit -= 1
    }
    answer + 1
  }
}
