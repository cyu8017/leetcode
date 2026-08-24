// LeetCode 2076 - Process Restricted Friend Requests
// https://leetcode.com/problems/process-restricted-friend-requests/

object Solution {
  def friendRequests(n: Int, restrictions: Array[Array[Int]], requests: Array[Array[Int]]): Array[Boolean] = {
    val parent = Array.tabulate(n)(identity)
    def find(x: Int): Int = {
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }
    def unite(a0: Int, b0: Int): Unit = {
      val a = find(a0)
      val b = find(b0)
      if (a != b) parent(a) = b
    }
    val ans = Array.ofDim[Boolean](requests.length)
    var i = 0
    while (i < requests.length) {
      val u = find(requests(i)(0))
      val v = find(requests(i)(1))
      var ok = true
      if (u != v) {
        var j = 0
        while (j < restrictions.length && ok) {
          val x = find(restrictions(j)(0))
          val y = find(restrictions(j)(1))
          if ((x == u && y == v) || (x == v && y == u)) ok = false
          j += 1
        }
      }
      ans(i) = ok
      if (ok) unite(u, v)
      i += 1
    }
    ans
  }
}
