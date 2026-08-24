// LeetCode 0807 - Max Increase to Keep City Skyline
// https://leetcode.com/problems/max-increase-to-keep-city-skyline/

object Solution {
  def maxIncreaseKeepingSkyline(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val rowMax = Array.ofDim[Int](m)
    val colMax = Array.ofDim[Int](n)
    var r = 0
    while (r < m) {
      var c = 0
      while (c < n) {
        rowMax(r) = math.max(rowMax(r), grid(r)(c))
        colMax(c) = math.max(colMax(c), grid(r)(c))
        c += 1
      }
      r += 1
    }
    var ans = 0
    r = 0
    while (r < m) {
      var c = 0
      while (c < n) {
        ans += math.min(rowMax(r), colMax(c)) - grid(r)(c)
        c += 1
      }
      r += 1
    }
    ans
  }
}
