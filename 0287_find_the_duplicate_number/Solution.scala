// LeetCode 0287 - Find the Duplicate Number
// https://leetcode.com/problems/find-the-duplicate-number/

object Solution {
  def findDuplicate(nums: Array[Int]): Int = {
    var slow = nums(0)
    var fast = nums(0)
    while ({
      slow = nums(slow)
      fast = nums(nums(fast))
      slow != fast
    }) ()
    slow = nums(0)
    while (slow != fast) {
      slow = nums(slow)
      fast = nums(fast)
    }
    slow
  }
}
