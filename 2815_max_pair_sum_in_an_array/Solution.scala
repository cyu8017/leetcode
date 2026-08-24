// LeetCode 2815 - Max Pair Sum in an Array
// https://leetcode.com/problems/max-pair-sum-in-an-array/

object Solution {
  def maxSum(nums: Array[Int]): Int = {
    val best = scala.collection.mutable.Map.empty[Int, Int]
    var ans = -1
    nums.foreach { v =>
      var x = v
      var md = 0
      while (x > 0) {
        md = math.max(md, x % 10)
        x /= 10
      }
      if (best.contains(md)) {
        ans = math.max(ans, best(md) + v)
        best(md) = math.max(best(md), v)
      } else best(md) = v
    }
    ans
  }
}
