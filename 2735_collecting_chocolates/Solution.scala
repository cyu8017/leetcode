// LeetCode 2735 - Collecting Chocolates
// https://leetcode.com/problems/collecting-chocolates/

object Solution {
  def minCost(nums: Array[Int], x: Int): Long = {
    val n = nums.length
    val best = nums.clone()
    var ans = 0L
    nums.foreach(v => ans += v)
    var rot = 1
    while (rot < n) {
      var cur = rot.toLong * x
      var i = 0
      while (i < n) {
        best(i) = math.min(best(i), nums((i + rot) % n))
        cur += best(i)
        i += 1
      }
      ans = math.min(ans, cur)
      rot += 1
    }
    ans
  }
}
