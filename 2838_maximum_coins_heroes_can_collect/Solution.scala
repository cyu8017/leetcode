// LeetCode 2838 - Maximum Coins Heroes Can Collect
// https://leetcode.com/problems/maximum-coins-heroes-can-collect/

object Solution {
  def maximumCoins(heroes: Array[Int], monsters: Array[Int], coins: Array[Int]): Array[Long] = {
    val n = monsters.length
    val idx = (0 until n).toArray.sortBy(monsters)
    val pref = Array.fill(n + 1)(0L)
    val ms = Array.fill(n)(0)
    for (i <- 0 until n) {
      ms(i) = monsters(idx(i))
      pref(i + 1) = pref(i) + coins(idx(i))
    }
    heroes.map { h =>
      pref(upperBound(ms, h))
    }
  }

  private def upperBound(a: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) >>> 1
      if (a(mid) <= x) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
