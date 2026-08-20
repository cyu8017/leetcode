// LeetCode 1250 - Check If It Is a Good Array
// https://leetcode.com/problems/check-if-it-is-a-good-array/

object Solution {
  def isGoodArray(nums: Array[Int]): Boolean = {
    def gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)
    nums.reduce(gcd) == 1
  }
}
