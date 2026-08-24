// LeetCode 3200 - Maximum Height of a Triangle
// https://leetcode.com/problems/maximum-height-of-a-triangle/

object Solution {
  def maxHeightOfTriangle(red: Int, blue: Int): Int = {
    var ans = 0
    var k = 0
    while (k < 2) {
      val c = Array(red, blue)
      var i = 1
      var j = k
      while (i <= c(j)) {
        c(j) -= i
        ans = math.max(ans, i)
        i += 1
        j ^= 1
      }
      k += 1
    }
    ans
  }
}
