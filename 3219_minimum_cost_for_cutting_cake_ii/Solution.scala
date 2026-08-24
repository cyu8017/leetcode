// LeetCode 3219 - Minimum Cost for Cutting Cake II
// https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii/

object Solution {
  def minimumCost(m: Int, n: Int, horizontalCut: Array[Int], verticalCut: Array[Int]): Long = {
    java.util.Arrays.sort(horizontalCut)
    reverse(horizontalCut)
    java.util.Arrays.sort(verticalCut)
    reverse(verticalCut)
    var i = 0
    var j = 0
    var h = 1
    var v = 1
    var ans = 0L
    while (i < m - 1 || j < n - 1) {
      if (j == n - 1 || (i < m - 1 && horizontalCut(i) > verticalCut(j))) {
        ans += horizontalCut(i).toLong * v
        h += 1; i += 1
      } else {
        ans += verticalCut(j).toLong * h
        v += 1; j += 1
      }
    }
    ans
  }

  def reverse(a: Array[Int]): Unit = {
    var l = 0
    var r = a.length - 1
    while (l < r) {
      val t = a(l); a(l) = a(r); a(r) = t
      l += 1; r -= 1
    }
  }
}
