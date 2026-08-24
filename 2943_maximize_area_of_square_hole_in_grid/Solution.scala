// LeetCode 2943 - Maximize Area of Square Hole in Grid
// https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

object Solution {
  private def maxGap(bars0: Array[Int]): Int = {
    if (bars0.length == 0) return 1
    val bars = bars0.clone()
    scala.util.Sorting.quickSort(bars)
    var best = 1
    var cur = 1
    var i = 1
    while (i < bars.length) {
      if (bars(i) == bars(i - 1) + 1) cur += 1
      else cur = 1
      if (cur > best) best = cur
      i += 1
    }
    best + 1
  }

  def maximizeSquareHoleArea(n: Int, m: Int, hBars: Array[Int], vBars: Array[Int]): Int = {
    var side = maxGap(hBars)
    val vs = maxGap(vBars)
    if (vs < side) side = vs
    side * side
  }
}
