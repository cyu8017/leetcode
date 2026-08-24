// LeetCode 3978 - Unique Middle Element
// https://leetcode.com/problems/unique-middle-element/

object Solution {
  def isMiddleElementUnique(nums: Array[Int]): Boolean = {
    val mid = nums(nums.length / 2)
    var cnt = 0
    for (x <- nums) if (x == mid) cnt += 1
    cnt == 1
  }
}
