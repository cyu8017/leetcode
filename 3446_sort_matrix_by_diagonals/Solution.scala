// LeetCode 3446 - Sort Matrix by Diagonals
// https://leetcode.com/problems/sort-matrix-by-diagonals/

object Solution {
  def sortMatrix(grid: Array[Array[Int]]): Array[Array[Int]] = {
    val n = grid.length
    val diags = scala.collection.mutable.Map.empty[Int, java.util.ArrayList[Integer]]
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        val list = diags.getOrElseUpdate(i - j, new java.util.ArrayList[Integer]())
        list.add(grid(i)(j))
        j += 1
      }
      i += 1
    }
    diags.foreach { case (key, value) =>
      if (key >= 0) java.util.Collections.sort(value, java.util.Collections.reverseOrder[Integer]())
      else java.util.Collections.sort(value)
    }
    val idx = scala.collection.mutable.Map.empty[Int, Int]
    i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        val k = i - j
        val pos = idx.getOrElse(k, 0)
        grid(i)(j) = diags(k).get(pos)
        idx(k) = pos + 1
        j += 1
      }
      i += 1
    }
    grid
  }
}
