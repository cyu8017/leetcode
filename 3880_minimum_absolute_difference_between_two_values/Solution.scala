// LeetCode 3880 - Minimum Absolute Difference Between Two Values
// https://leetcode.com/problems/minimum-absolute-difference-between-two-values/

object Solution {
  def minAbsoluteDifference(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = n + 1
    val last = Array(-ans, -ans, -ans)
    var i = 0
    while (i < n) {
      val x = nums(i)
      if (x != 0) {
        ans = math.min(ans, i - last(3 - x))
        last(x) = i
      }
      i += 1
    }
    if (ans > n) -1 else ans
  }
}
