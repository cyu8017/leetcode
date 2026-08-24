// LeetCode 0905 - Sort Array By Parity
// https://leetcode.com/problems/sort-array-by-parity/

object Solution {
  def sortArrayByParity(nums: Array[Int]): Array[Int] = {
    var i = 0
    var j = 0
    while (j < nums.length) {
      if (nums(j) % 2 == 0) {
        val tmp = nums(i)
        nums(i) = nums(j)
        nums(j) = tmp
        i += 1
      }
      j += 1
    }
    nums
  }
}
