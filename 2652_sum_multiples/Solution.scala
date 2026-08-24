// LeetCode 2652 - Sum Multiples
// https://leetcode.com/problems/sum-multiples/

object Solution {
  def sumOfMultiples(n: Int): Int = {
    var ans = 0
    var i = 1
    while (i <= n) {
      if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0) ans += i
      i += 1
    }
    ans
  }
}
