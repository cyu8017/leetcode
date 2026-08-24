// LeetCode 2817 - Minimum Absolute Difference Between Elements With Constraint
// https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

object Solution {
  def minAbsoluteDifference(nums: List[Int], x: Int): Int = {
    if (x == 0) {
      var ans0 = Int.MaxValue
      var i = 1
      while (i < nums.length) {
        ans0 = math.min(ans0, math.abs(nums(i) - nums(i - 1)))
        i += 1
      }
      return ans0
    }
    var ans = Int.MaxValue
    val arr = scala.collection.mutable.TreeSet.empty[Int]
    var i = x
    while (i < nums.length) {
      arr += nums(i - x)
      val cur = nums(i)
      arr.rangeFrom(cur).headOption.foreach(ceil => ans = math.min(ans, ceil - cur))
      arr.rangeTo(cur).lastOption.foreach(floor => ans = math.min(ans, cur - floor))
      i += 1
    }
    ans
  }
}
