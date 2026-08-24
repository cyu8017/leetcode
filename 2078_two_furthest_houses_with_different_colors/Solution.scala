// LeetCode 2078 - Two Furthest Houses With Different Colors
// https://leetcode.com/problems/two-furthest-houses-with-different-colors/

object Solution {
  def maxDistance(colors: Array[Int]): Int = {
    val n = colors.length
    var ans = 0
    var i = 0
    while (i < n) {
      if (colors(i) != colors(0)) ans = math.max(ans, i)
      if (colors(i) != colors(n - 1)) ans = math.max(ans, n - 1 - i)
      i += 1
    }
    ans
  }
}
