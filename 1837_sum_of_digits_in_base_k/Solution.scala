// LeetCode 1837 - Sum of Digits in Base K
// https://leetcode.com/problems/sum-of-digits-in-base-k/

object Solution {
  def sumBase(n: Int, k: Int): Int = {
    var x = n
    var total = 0
    while (x > 0) {
      total += x % k
      x /= k
    }
    total
  }
}
