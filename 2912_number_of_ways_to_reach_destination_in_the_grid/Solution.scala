// LeetCode 2912 - Number of Ways to Reach Destination in the Grid
// https://leetcode.com/problems/number-of-ways-to-reach-destination-in-the-grid/

object Solution {
  def numberOfWays(n: Int, m: Int, k: Int, source: Array[Int], dest: Array[Int]): Int = {
    val mod = 1000000007
    val sx = source(0)
    val sy = source(1)
    val tx = dest(0)
    val ty = dest(1)
    var same = 0L
    var row = 0L
    var col = 0L
    var other = 0L
    if (sx == tx && sy == ty) same = 1
    else if (sx == tx) row = 1
    else if (sy == ty) col = 1
    else other = 1
    for (_ <- 0 until k) {
      val ns = (row * (m - 1) + col * (n - 1)) % mod
      val nr = (same + row * (m - 2) % mod + other * (n - 1) % mod) % mod
      val nc = (same + col * (n - 2) % mod + other * (m - 1) % mod) % mod
      val no = (row * (n - 1) + col * (m - 1) + other * (n + m - 4) % mod) % mod
      same = ns
      row = nr
      col = nc
      other = no
    }
    if (sx == tx && sy == ty) same.toInt
    else if (sx == tx) row.toInt
    else if (sy == ty) col.toInt
    else other.toInt
  }
}
