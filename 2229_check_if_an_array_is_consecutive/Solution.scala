// LeetCode 2229 - Check if an Array Is Consecutive
// https://leetcode.com/problems/check-if-an-array-is-consecutive/

object Solution {
  def isConsecutive(nums: Array[Int]): Boolean = {
    var mn = nums(0)
    var mx = nums(0)
    val seen = scala.collection.mutable.HashSet.empty[Int]
    for (x <- nums) {
      if (!seen.add(x)) return false
      mn = math.min(mn, x)
      mx = math.max(mx, x)
    }
    mx - mn + 1 == nums.length
  }
}
