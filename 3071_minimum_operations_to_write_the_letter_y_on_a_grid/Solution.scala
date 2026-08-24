// LeetCode 3071 - Minimum Operations to Write the Letter Y on a Grid
// https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/

object Solution {
  def minimumOperationsToWriteY(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    val cnt1 = new Array[Int](3)
    val cnt2 = new Array[Int](3)
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        val x = grid(i)(j)
        val a = i == j && i <= n / 2
        val b = i + j == n - 1 && i <= n / 2
        val c = j == n / 2 && i >= n / 2
        if (a || b || c) cnt1(x) += 1
        else cnt2(x) += 1
        j += 1
      }
      i += 1
    }
    var ans = n * n
    i = 0
    while (i < 3) {
      var j = 0
      while (j < 3) {
        if (i != j) ans = math.min(ans, n * n - cnt1(i) - cnt2(j))
        j += 1
      }
      i += 1
    }
    ans
  }
}
