// LeetCode 1608 - Special Array With X Elements Greater Than or Equal X
// https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

object Solution {
  def specialArray(nums: Array[Int]): Int = {
    (0 to nums.length).find(x => nums.count(_ >= x) == x).getOrElse(-1)
  }
}
