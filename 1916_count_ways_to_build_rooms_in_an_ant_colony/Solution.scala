// LeetCode 1916 - Count Ways to Build Rooms in an Ant Colony
// https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/

object Solution {
  def waysToBuildRooms(prevRoom: Array[Int]): Int = {
    val MOD = 1000000007
    val n = prevRoom.length
    val children = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (room <- 0 until n if prevRoom(room) != -1) {
      children(prevRoom(room)) += room
    }
    val fact = Array.fill(n + 1)(1L)
    val invFact = Array.fill(n + 1)(1L)
    for (i <- 1 to n) fact(i) = fact(i - 1) * i % MOD
    invFact(n) = modPow(fact(n), MOD - 2, MOD)
    for (i <- n until 0 by -1) invFact(i - 1) = invFact(i) * i % MOD

    def comb(a: Int, b: Int): Long =
      fact(a) * invFact(b) % MOD * invFact(a - b) % MOD

    def dfs(node: Int): (Int, Long) = {
      var size = 0
      var ways = 1L
      for (child <- children(node)) {
        val (childSize, childWays) = dfs(child)
        ways = ways * childWays % MOD * comb(size + childSize, childSize) % MOD
        size += childSize
      }
      (size + 1, ways)
    }

    dfs(0)._2.toInt
  }

  private def modPow(base: Long, exp: Long, mod: Int): Long = {
    var b = base % mod
    var e = exp
    var res = 1L
    while (e > 0) {
      if ((e & 1) == 1) res = res * b % mod
      b = b * b % mod
      e >>= 1
    }
    res
  }
}
