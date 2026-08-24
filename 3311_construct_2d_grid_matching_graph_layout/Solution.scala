// LeetCode 3311 - Construct 2D Grid Matching Graph Layout
// https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/

object Solution {
  def constructGridLayout(n: Int, edges: Array[Array[Int]]): Array[Array[Int]] = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- edges) {
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    val deg = Array.tabulate(n)(i => g(i).length)
    var start = 0
    var i = 0
    while (i < n) {
      if (deg(i) == 1) { start = i; i = n }
      else {
        if (deg(i) == 2) start = i
        i += 1
      }
    }
    val vis = new Array[Boolean](n)
    val row = scala.collection.mutable.ArrayBuffer.empty[Int]
    var cur = start
    var prev = -1
    var done = false
    while (!done) {
      row += cur
      vis(cur) = true
      var next = -1
      for (v <- g(cur)) {
        if (v != prev && !vis(v) && deg(v) <= 3) {
          next = v
          if (deg(v) < 4) { /* prefer */ }
        }
      }
      if (next == -1) done = true
      else {
        prev = cur
        cur = next
      }
    }
    var width = row.length
    var height = if (width != 0) n / width else n
    if (width == 0 || width * height != n) {
      var w = 1
      var found = false
      while (w <= n && !found) {
        if (n % w == 0) {
          width = w
          height = n / w
          found = true
        }
        w += 1
      }
    }
    val grid = Array.ofDim[Int](height, width)
    i = 0
    while (i < n) {
      grid(i / width)(i % width) = i
      i += 1
    }
    grid
  }
}
