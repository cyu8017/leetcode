// LeetCode 3840 - House Robber V
// https://leetcode.com/problems/house-robber-v/

object Solution {
  def rob(nums: Array[Int], colors: Array[Int]): Long = {
    val n = nums.length
    var f = 0L
    var g = nums(0).toLong
    var i = 1
    while (i < n) {
      if (colors(i - 1) == colors(i)) {
        val nf = math.max(f, g)
        g = f + nums(i)
        f = nf
      } else {
        val nf = math.max(f, g)
        g = nf + nums(i)
        f = nf
      }
      i += 1
    }
    math.max(f, g)
  }
}
