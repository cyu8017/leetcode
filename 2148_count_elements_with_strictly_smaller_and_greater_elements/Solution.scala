// LeetCode 2148 - Count Elements With Strictly Smaller and Greater Elements
// https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

object Solution {
  def countElements(nums: Array[Int]): Int = {
    var mn = nums(0)
    var mx = nums(0)
    nums.foreach { x =>
      mn = math.min(mn, x)
      mx = math.max(mx, x)
    }
    nums.count(x => x > mn && x < mx)
  }
}
