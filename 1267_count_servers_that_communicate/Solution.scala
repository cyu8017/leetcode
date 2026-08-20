// LeetCode 1267 - Count Servers that Communicate
// https://leetcode.com/problems/count-servers-that-communicate/

object Solution {
  def countServers(grid: Array[Array[Int]]): Int = {
    val rows = grid.map(_.sum)
    val cols = grid(0).indices.map(c => grid.map(_(c)).sum)
    var ans = 0
    for (r <- grid.indices; c <- grid(0).indices if grid(r)(c) == 1 && (rows(r) > 1 || cols(c) > 1)) ans += 1
    ans
  }
}
