// LeetCode 0280 - Wiggle Sort
// https://leetcode.com/problems/wiggle-sort/

object Solution {
  def wiggleSort(nums: Array[Int]): Unit = {
    var index = 1
    while (index < nums.length) {
      if (index % 2 == 1 && nums(index) < nums(index - 1)) {
        val tmp = nums(index)
        nums(index) = nums(index - 1)
        nums(index - 1) = tmp
      } else if (index % 2 == 0 && nums(index) > nums(index - 1)) {
        val tmp = nums(index)
        nums(index) = nums(index - 1)
        nums(index - 1) = tmp
      }
      index += 1
    }
  }
}
