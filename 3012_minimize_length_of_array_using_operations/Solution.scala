// LeetCode 3012 - Minimize Length of Array Using Operations
// https://leetcode.com/problems/minimize-length-of-array-using-operations/

object Solution {
  def minimumArrayLength(nums: Array[Int]): Int = {
    var mi = nums(0)
    for (x <- nums) if (x < mi) mi = x
    var cnt = 0
    for (x <- nums) {
      if (x % mi != 0) return 1
      if (x == mi) cnt += 1
    }
    (cnt + 1) / 2
  }
}
