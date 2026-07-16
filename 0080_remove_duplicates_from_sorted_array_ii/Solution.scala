// LeetCode 0080 - Remove Duplicates from Sorted Array II
// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

object Solution {
  def removeDuplicates(nums: Array[Int]): Int = {
    if (nums.length <= 2) {
      return nums.length
    }

    var write = 2
    var i = 2
    while (i < nums.length) {
      if (nums(i) != nums(write - 2)) {
        nums(write) = nums(i)
        write += 1
      }
      i += 1
    }

    write
  }
}
