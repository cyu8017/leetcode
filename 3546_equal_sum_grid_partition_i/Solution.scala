// LeetCode 3546 - Equal Sum Grid Partition I
// https://leetcode.com/problems/equal-sum-grid-partition-i/

object Solution {
  def canPartitionGrid(grid: Array[Array[Int]]): Boolean = {
    var s = 0L
    for (row <- grid; x <- row) s += x
    if (s % 2 != 0) return false
    val m = grid.length
    val n = grid(0).length
    var pre = 0L
    var i = 0
    while (i < m) {
      for (x <- grid(i)) pre += x
      if (pre * 2 == s && i + 1 < m) return true
      i += 1
    }
    pre = 0
    var j = 0
    while (j < n) {
      i = 0
      while (i < m) { pre += grid(i)(j); i += 1 }
      if (pre * 2 == s && j + 1 < n) return true
      j += 1
    }
    false
  }
}
