// LeetCode 0137 - Single Number II
// https://leetcode.com/problems/single-number-ii/

object Solution {
  def singleNumber(nums: Array[Int]): Int = {
    var ones = 0
    var twos = 0
    for (num <- nums) {
      ones = (ones ^ num) & ~twos
      twos = (twos ^ num) & ~ones
    }
    ones
  }
}
