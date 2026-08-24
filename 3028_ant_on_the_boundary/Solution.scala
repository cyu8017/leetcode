// LeetCode 3028 - Ant on the Boundary
// https://leetcode.com/problems/ant-on-the-boundary/

object Solution {
  def returnToBoundaryCount(nums: Array[Int]): Int = {
    var s = 0
    var ans = 0
    for (x <- nums) {
      s += x
      if (s == 0) ans += 1
    }
    ans
  }
}
