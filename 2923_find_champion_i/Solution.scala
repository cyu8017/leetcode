// LeetCode 2923 - Find Champion I
// https://leetcode.com/problems/find-champion-i/

object Solution {
  def findChampion(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    for (i <- 0 until n) {
      var win = true
      var j = 0
      while (j < n && win) {
        if (i != j && grid(i)(j) == 0) win = false
        j += 1
      }
      if (win) return i
    }
    -1
  }
}
