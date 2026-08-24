// LeetCode 4009 - Minimum Possible Maximum Waiting Time
// https://leetcode.com/problems/minimum-possible-maximum-waiting-time/

import scala.collection.mutable

object Solution {
  private var dem: Array[Int] = Array.empty
  private var n: Int = 0
  private var W: Int = 0
  private var bestServe: Int = 0
  private val memo = mutable.HashMap.empty[Long, Int]

  private def packKey(i: Int, f0: Int, f1: Int, d0: Int, d1: Int): Long =
    (((((i.toLong * 51 + f0) * 51 + f1) * 21 + d0) * 21) + d1)

  private def maxServe(i: Int, f0: Int, f1: Int, d0: Int, d1: Int): Int = {
    if (i == n) return i
    val key = packKey(i, f0, f1, d0, d1)
    if (memo.contains(key)) return memo(key)
    val need = dem(i)
    val can0 = f0 >= need
    val can1 = f1 >= need
    var best = i
    if (!can0 && !can1) {
      memo(key) = best
      return best
    }
    if (can0) {
      val nd1 = if (d1 > d0) d1 - d0 else 0
      best = math.max(best, maxServe(i + 1, f0 - need, f1, need, nd1))
    }
    if (can1) {
      val nd0 = if (d0 > d1) d0 - d1 else 0
      best = math.max(best, maxServe(i + 1, f0, f1 - need, nd0, need))
    }
    memo(key) = best
    best
  }

  private def canWithW(i: Int, f0: Int, f1: Int, d0: Int, d1: Int): Boolean = {
    if (i >= bestServe) return true
    if (i == n) return true
    val key = packKey(i, f0, f1, d0, d1)
    if (memo.contains(key)) return memo(key) == 2
    val need = dem(i)
    val can0 = f0 >= need
    val can1 = f1 >= need
    var ok = false
    if (!can0 && !can1) {
      memo(key) = 1
      return false
    }
    if (can0 && d0 <= W) {
      val nd1 = if (d1 > d0) d1 - d0 else 0
      if (canWithW(i + 1, f0 - need, f1, need, nd1)) ok = true
    }
    if (!ok && can1 && d1 <= W) {
      val nd0 = if (d0 > d1) d0 - d1 else 0
      if (canWithW(i + 1, f0, f1 - need, nd0, need)) ok = true
    }
    memo(key) = if (ok) 2 else 1
    ok
  }

  def minMaxWaitingTime(demand: Array[Int], fuel: Array[Int]): Int = {
    dem = demand
    n = demand.length
    val f0 = fuel(0)
    val f1 = fuel(1)
    if (f0 < demand(0) && f1 < demand(0)) return -1
    memo.clear()
    bestServe = maxServe(0, f0, f1, 0, 0)
    if (bestServe == 0) return -1
    var lo = 0
    var hi = 0
    for (x <- demand) hi += x
    var ans = hi
    while (lo <= hi) {
      val mid = (lo + hi) / 2
      W = mid
      memo.clear()
      if (canWithW(0, f0, f1, 0, 0)) {
        ans = mid
        hi = mid - 1
      } else lo = mid + 1
    }
    ans
  }
}
