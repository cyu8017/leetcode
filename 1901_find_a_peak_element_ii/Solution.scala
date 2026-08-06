// LeetCode 1901 - Find a Peak Element II
// https://leetcode.com/problems/find-a-peak-element-ii/

object Solution {
  def findPeakGrid(mat: Array[Array[Int]]): Array[Int] = {
    val rows = mat.length
    val cols = mat(0).length
    var lo = 0
    var hi = cols - 1
    while (lo <= hi) {
      val mid = (lo + hi) / 2
      var maxRow = 0
      for (r <- 1 until rows) if (mat(r)(mid) > mat(maxRow)(mid)) maxRow = r
      val left = if (mid > 0) mat(maxRow)(mid - 1) else -1
      val right = if (mid + 1 < cols) mat(maxRow)(mid + 1) else -1
      if (mat(maxRow)(mid) >= left && mat(maxRow)(mid) >= right) return Array(maxRow, mid)
      if (left > mat(maxRow)(mid)) hi = mid - 1
      else lo = mid + 1
    }
    Array(0, 0)
  }
}
