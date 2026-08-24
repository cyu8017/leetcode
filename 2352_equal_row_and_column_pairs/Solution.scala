// LeetCode 2352 - Equal Row and Column Pairs
// https://leetcode.com/problems/equal-row-and-column-pairs/

object Solution {
  def equalPairs(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    val freq = scala.collection.mutable.Map.empty[String, Int]
    var i = 0
    while (i < n) {
      val key = grid(i).mkString(",")
      freq(key) = freq.getOrElse(key, 0) + 1
      i += 1
    }
    var ans = 0
    val col = Array.fill(n)(0)
    var j = 0
    while (j < n) {
      i = 0
      while (i < n) {
        col(i) = grid(i)(j)
        i += 1
      }
      ans += freq.getOrElse(col.mkString(","), 0)
      j += 1
    }
    ans
  }
}
