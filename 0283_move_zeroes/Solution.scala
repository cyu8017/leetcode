// LeetCode 0283 - Move Zeroes
// https://leetcode.com/problems/move-zeroes/

object Solution {
  def moveZeroes(nums: Array[Int]): Unit = {
    var insert = 0
    for (num <- nums) {
      if (num != 0) {
        nums(insert) = num
        insert += 1
      }
    }
    var index = insert
    while (index < nums.length) {
      nums(index) = 0
      index += 1
    }
  }
}
