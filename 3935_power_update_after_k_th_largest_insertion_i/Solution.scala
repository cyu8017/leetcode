// LeetCode 3935 - Power Update After K-th Largest Insertion I
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-i/

import scala.collection.mutable

object Solution {
  private def merge(st: mutable.TreeMap[Int, Int], x: Int, v: Int): Unit = {
    val c = st.getOrElse(x, 0)
    if (c + v == 0) st.remove(x)
    else st(x) = c + v
  }

  def powerUpdate(nums: Array[Int], p: Int, queries: Array[Array[Int]]): Array[Int] = {
    val L = mutable.TreeMap.empty[Int, Int]
    val R = mutable.TreeMap.empty[Int, Int]
    var sz1 = 0
    var sz2 = nums.length
    for (x <- nums) merge(R, x, 1)
    val mod = 1000000007
    val ans = new Array[Int](queries.length)
    var power = p
    var qi = 0
    while (qi < queries.length) {
      val `val` = queries(qi)(0)
      val k = queries(qi)(1)
      merge(R, `val`, 1)
      sz2 += 1
      var node = R.firstKey
      merge(R, node, -1)
      sz2 -= 1
      merge(L, node, 1)
      sz1 += 1
      while (sz2 < k) {
        node = L.lastKey
        merge(L, node, -1)
        sz1 -= 1
        merge(R, node, 1)
        sz2 += 1
      }
      while (sz2 > k) {
        node = R.firstKey
        merge(R, node, -1)
        sz2 -= 1
        merge(L, node, 1)
        sz1 += 1
      }
      val x = R.firstKey
      power = qpow(power, x, mod)
      ans(qi) = power
      qi += 1
    }
    ans
  }

  private def qpow(base: Long, exp: Int, mod: Int): Int = {
    var a = base
    var b = exp
    var ans = 1L
    while (b > 0) {
      if ((b & 1) != 0) ans = ans * a % mod
      a = a * a % mod
      b >>= 1
    }
    ans.toInt
  }
}
