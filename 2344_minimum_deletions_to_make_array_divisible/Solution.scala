// LeetCode 2344 - Minimum Deletions to Make Array Divisible
// https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

object Solution {
  def minOperations(nums: Array[Int], numsDivide: Array[Int]): Int = {
    var g = numsDivide(0)
    var i = 1
    while (i < numsDivide.length) {
      g = gcd(g, numsDivide(i))
      i += 1
    }
    java.util.Arrays.sort(nums)
    i = 0
    while (i < nums.length) {
      if (g % nums(i) == 0) return i
      i += 1
    }
    -1
  }

  private def gcd(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }
}
