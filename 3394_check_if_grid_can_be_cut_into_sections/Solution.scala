// LeetCode 3394 - Check if Grid can be Cut into Sections
// https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

object Solution {
  private def checkCut(rects: Array[Array[Int]], axis: Int): Boolean = {
    val arr = Array.tabulate(rects.length) { i =>
      if (axis == 0) Array(rects(i)(0), rects(i)(2))
      else Array(rects(i)(1), rects(i)(3))
    }
    scala.util.Sorting.stableSort(arr, (x: Array[Int], y: Array[Int]) =>
      if (x(0) == y(0)) x(1) < y(1) else x(0) < y(0)
    )
    var cuts = 0
    var end = arr(0)(1)
    var i = 1
    while (i < arr.length) {
      if (arr(i)(0) >= end) {
        cuts += 1
        end = arr(i)(1)
        if (cuts >= 2) return true
      } else if (arr(i)(1) > end) {
        end = arr(i)(1)
      }
      i += 1
    }
    false
  }

  def checkValidCuts(n: Int, rectangles: Array[Array[Int]]): Boolean =
    checkCut(rectangles, 0) || checkCut(rectangles, 1)
}
