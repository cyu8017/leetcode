// LeetCode 0470 - Implement Rand10() Using Rand7()
// https://leetcode.com/problems/implement-rand10-using-rand7/

def rand7(): Int =
  throw new RuntimeException("rand7 must be provided by the test harness")

object Solution {
  def rand10(): Int = {
    var num = 0
    do {
      num = (rand7() - 1) * 7 + rand7()
    } while (num > 40)
    (num - 1) % 10 + 1
  }
}
