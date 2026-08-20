// LeetCode 1295 - Find Numbers with Even Number of Digits
// https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

object Solution {
  def findNumbers(nums: Array[Int]): Int =
    nums.count(value => value.toString.length % 2 == 0)
}
