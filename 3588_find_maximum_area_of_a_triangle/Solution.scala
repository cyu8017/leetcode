// LeetCode 3588 - Find Maximum Area of a Triangle
// https://leetcode.com/problems/find-maximum-area-of-a-triangle/

object Solution {
  def calc(coords: Array[Array[Int]]): Long = {
    var mn = 1000000000
    var mx = 0
    val f = scala.collection.mutable.HashMap.empty[Int, Int]
    val g = scala.collection.mutable.HashMap.empty[Int, Int]
    for (c <- coords) {
      val x = c(0)
      val y = c(1)
      mn = math.min(mn, x)
      mx = math.max(mx, x)
      if (f.contains(x)) {
        f(x) = math.min(f(x), y)
        g(x) = math.max(g(x), y)
      } else {
        f(x) = y
        g(x) = y
      }
    }
    var ans = 0L
    for ((x, y) <- f) {
      val d = g(x) - y
      ans = math.max(ans, 1L * d * math.max(mx - x, x - mn))
    }
    ans
  }

  def maxArea(coords: Array[Array[Int]]): Long = {
    var ans = calc(coords)
    for (c <- coords) {
      val t = c(0)
      c(0) = c(1)
      c(1) = t
    }
    ans = math.max(ans, calc(coords))
    if (ans > 0) ans else -1
  }
}
