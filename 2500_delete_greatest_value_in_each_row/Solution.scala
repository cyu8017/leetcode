// LeetCode 2500 - Delete Greatest Value in Each Row
// https://leetcode.com/problems/delete-greatest-value-in-each-row/

object Solution {
  def deleteGreatestValue(grid: Array[Array[Int]]): Int = {
    grid.foreach(row => scala.util.Sorting.quickSort(row))
    var ans = 0
    val n = grid(0).length
    var c = 0
    while (c < n) {
      var mx = 0
      var r = 0
      while (r < grid.length) {
        if (grid(r)(c) > mx) mx = grid(r)(c)
        r += 1
      }
      ans += mx
      c += 1
    }
    ans
  }
}
