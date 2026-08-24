// LeetCode 2210 - Count Hills and Valleys in an Array
// https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

object Solution {
  def countHillValley(nums: Array[Int]): Int = {
    val compact = scala.collection.mutable.ArrayBuffer(nums(0))
    var i = 1
    while (i < nums.length) {
      if (nums(i) != compact.last) compact += nums(i)
      i += 1
    }
    var ans = 0
    i = 1
    while (i + 1 < compact.length) {
      if ((compact(i) > compact(i - 1) && compact(i) > compact(i + 1)) ||
          (compact(i) < compact(i - 1) && compact(i) < compact(i + 1)))
        ans += 1
      i += 1
    }
    ans
  }
}
