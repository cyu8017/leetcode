// LeetCode 1186 - Maximum Subarray Sum with One Deletion
// https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

object Solution {
  def maximumSum(arr: Array[Int]): Int = {
    var keep = arr(0)
    var delete = arr(0)
    var ans = arr(0)
    for (i <- 1 until arr.length) {
      val x = arr(i)
      delete = math.max(keep, delete + x)
      keep = math.max(keep + x, x)
      ans = math.max(ans, math.max(keep, delete))
    }
    ans
  }
}
