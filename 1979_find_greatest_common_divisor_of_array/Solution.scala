// LeetCode 1979 - Find Greatest Common Divisor of Array
// https://leetcode.com/problems/find-greatest-common-divisor-of-array/

object Solution {
  def findGCD(nums: Array[Int]): Int = {
    def gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)
    gcd(nums.min, nums.max)
  }
}
