// LeetCode 2711 - Difference of Number of Distinct Values on Diagonals
// https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

object Solution {
  def differenceOfDistinctValues(grid: Array[Array[Int]]): Array[Array[Int]] = {
    val m = grid.length
    val n = grid(0).length
    val ans = Array.ofDim[Int](m, n)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        val top = scala.collection.mutable.HashSet.empty[Int]
        val bot = scala.collection.mutable.HashSet.empty[Int]
        var r = i - 1
        var c = j - 1
        while (r >= 0 && c >= 0) {
          top += grid(r)(c)
          r -= 1
          c -= 1
        }
        r = i + 1
        c = j + 1
        while (r < m && c < n) {
          bot += grid(r)(c)
          r += 1
          c += 1
        }
        ans(i)(j) = math.abs(top.size - bot.size)
        j += 1
      }
      i += 1
    }
    ans
  }
}
