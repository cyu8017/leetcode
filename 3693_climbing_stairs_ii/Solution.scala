// LeetCode 3693 - Climbing Stairs II
// https://leetcode.com/problems/climbing-stairs-ii/

object Solution {
  def climbStairs(n: Int, costs: Array[Int]): Int = {
    val inf = 1000000000
    val f = Array.fill(n + 1)(inf)
    f(0) = 0
    var i = 1
    while (i <= n) {
      val x = costs(i - 1)
      var j = math.max(0, i - 3)
      while (j < i) {
        f(i) = math.min(f(i), f(j) + x + (i - j) * (i - j))
        j += 1
      }
      i += 1
    }
    f(n)
  }
}
