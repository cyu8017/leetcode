// LeetCode 3417 - Zigzag Grid Traversal With Skip
// https://leetcode.com/problems/zigzag-grid-traversal-with-skip/

object Solution {
  def zigzagTraversal(grid: Array[Array[Int]]): Array[Int] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    var skip = false
    var i = 0
    while (i < grid.length) {
      val row = grid(i)
      if (i % 2 == 0) {
        row.foreach { v =>
          if (!skip) ans += v
          skip = !skip
        }
      } else {
        var j = row.length - 1
        while (j >= 0) {
          if (!skip) ans += row(j)
          skip = !skip
          j -= 1
        }
      }
      i += 1
    }
    ans.toArray
  }
}
