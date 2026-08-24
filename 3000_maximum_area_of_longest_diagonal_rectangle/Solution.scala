// LeetCode 3000 - Maximum Area of Longest Diagonal Rectangle
// https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/

object Solution {
  def areaOfMaxDiagonal(dimensions: Array[Array[Int]]): Int = {
    var ans = 0
    var mx = 0
    for (d <- dimensions) {
      val l = d(0)
      val w = d(1)
      val t = l * l + w * w
      if (mx < t) { mx = t; ans = l * w }
      else if (mx == t) ans = math.max(ans, l * w)
    }
    ans
  }
}
