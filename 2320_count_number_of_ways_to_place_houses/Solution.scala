// LeetCode 2320 - Count Number of Ways to Place Houses
// https://leetcode.com/problems/count-number-of-ways-to-place-houses/

object Solution {
  def countHousePlacements(n: Int): Int = {
    val mod = 1000000007
    var a = 1L
    var b = 1L
    var i = 1
    while (i <= n) {
      val na = (a + b) % mod
      b = a
      a = na
      i += 1
    }
    val ways = (a + b) % mod
    (ways * ways % mod).toInt
  }
}
