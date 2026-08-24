// LeetCode 2778 - Sum of Squares of Special Elements
// https://leetcode.com/problems/sum-of-squares-of-special-elements/

object Solution {
  def sumOfSquares(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 0
    var i = 0
    while (i < n) {
      if (n % (i + 1) == 0) ans += nums(i) * nums(i)
      i += 1
    }
    ans
  }
}
