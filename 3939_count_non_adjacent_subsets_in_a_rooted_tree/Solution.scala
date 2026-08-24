// LeetCode 3939 - Count Non-Adjacent Subsets in a Rooted Tree
// https://leetcode.com/problems/count-non-adjacent-subsets-in-a-rooted-tree/

import scala.collection.mutable

object Solution {
  def countNonAdjacentSubsets(parent: Array[Int], nums: Array[Int], k: Int): Int = {
    val mod = 1000000007L
    val n = parent.length
    val children = Array.fill(n)(mutable.ArrayBuffer.empty[Int])
    var i = 1
    while (i < n) {
      children(parent(i)) += i
      i += 1
    }
    val dp0 = new Array[Array[Long]](n)
    val dp1 = new Array[Array[Long]](n)
    var u = n - 1
    while (u >= 0) {
      var a = new Array[Long](k)
      var b = new Array[Long](k)
      a(0) = 1
      b(((nums(u) % k) + k) % k) = 1
      for (v <- children(u)) {
        val na = new Array[Long](k)
        val nb = new Array[Long](k)
        var x = 0
        while (x < k) {
          var y = 0
          while (y < k) {
            val allChild = (dp0(v)(y) + dp1(v)(y)) % mod
            na((x + y) % k) = (na((x + y) % k) + a(x) * allChild) % mod
            nb((x + y) % k) = (nb((x + y) % k) + b(x) * dp0(v)(y)) % mod
            y += 1
          }
          x += 1
        }
        a = na
        b = nb
      }
      dp0(u) = a
      dp1(u) = b
      u -= 1
    }
    var ans = (dp0(0)(0) + dp1(0)(0) - 1) % mod
    if (ans < 0) ans += mod
    ans.toInt
  }
}
