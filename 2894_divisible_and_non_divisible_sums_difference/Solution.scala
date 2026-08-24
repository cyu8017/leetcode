// LeetCode 2894 - Divisible and Non-divisible Sums Difference
// https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

object Solution {
  def differenceOfSums(n: Int, m: Int): Int = {
    var num1 = 0
    var num2 = 0
    for (i <- 1 to n) {
      if (i % m == 0) num2 += i
      else num1 += i
    }
    num1 - num2
  }
}
