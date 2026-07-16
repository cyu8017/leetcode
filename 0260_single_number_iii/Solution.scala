// LeetCode 0260 - Single Number III
// https://leetcode.com/problems/single-number-iii/

object Solution {
  def singleNumber(nums: Array[Int]): Array[Int] = {
    var xorAll = 0
    nums.foreach(num => xorAll ^= num)
    val diff = xorAll & -xorAll
    var first = 0
    var second = 0
    nums.foreach { num =>
      if ((num & diff) != 0) {
        first ^= num
      } else {
        second ^= num
      }
    }
    Array(first, second)
  }
}
