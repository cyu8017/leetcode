object Solution {
  def countNegatives(grid: Array[Array[Int]]): Int = grid.map { row =>
    var lo = 0; var hi = row.length
    while (lo < hi) { val mid = (lo + hi) >>> 1; if (row(mid) < 0) hi = mid else lo = mid + 1 }
    row.length - lo
  }.sum
}
