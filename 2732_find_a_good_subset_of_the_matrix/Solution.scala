// LeetCode 2732 - Find a Good Subset of the Matrix
// https://leetcode.com/problems/find-a-good-subset-of-the-matrix/

object Solution {
  def goodSubsetofBinaryMatrix(grid: Array[Array[Int]]): List[Int] = {
    val n = grid(0).length
    val first = scala.collection.mutable.LinkedHashMap.empty[Int, Int]
    var i = 0
    while (i < grid.length) {
      var mask = 0
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 1) mask |= 1 << j
        j += 1
      }
      if (mask == 0) return List(i)
      first.foreach { case (prev, a) =>
        if ((prev & mask) == 0) {
          val b = i
          return if (a < b) List(a, b) else List(b, a)
        }
      }
      if (!first.contains(mask)) first(mask) = i
      i += 1
    }
    List.empty[Int]
  }
}
