// LeetCode 0026 - Remove Duplicates from Sorted Array
// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

object Solution {
  def removeDuplicates(nums: Array[Int]): Int = {
    if (nums.isEmpty) {
      return 0
    }

    var write = 1
    var read = 1
    while (read < nums.length) {
      if (nums(read) != nums(write - 1)) {
        nums(write) = nums(read)
        write += 1
      }
      read += 1
    }

    write
  }
}
