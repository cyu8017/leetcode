// LeetCode 0027 - Remove Element
// https://leetcode.com/problems/remove-element/

object Solution {
  def removeElement(nums: Array[Int], value: Int): Int = {
    var write = 0
    var read = 0
    while (read < nums.length) {
      if (nums(read) != value) {
        nums(write) = nums(read)
        write += 1
      }
      read += 1
    }
    write
  }
}
