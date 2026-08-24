// LeetCode 3229 - Minimum Operations to Make Array Equal to Target
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/

object Solution {
  def minimumOperations(nums: Array[Int], target: Array[Int]): Long = {
    var f = math.abs(target(0) - nums(0)).toLong
    var i = 1
    while (i < target.length) {
      val x = target(i) - nums(i)
      val y = target(i - 1) - nums(i - 1)
      if (x.toLong * y > 0) {
        val d = math.abs(x) - math.abs(y)
        if (d > 0) f += d
      } else {
        f += math.abs(x)
      }
      i += 1
    }
    f
  }
}
