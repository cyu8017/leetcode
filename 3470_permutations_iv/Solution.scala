// LeetCode 3470 - Permutations IV
// https://leetcode.com/problems/permutations-iv/

object Solution {
  private var fact: Array[Long] = _
  private var used: Array[Boolean] = _
  private var ans: java.util.ArrayList[Integer] = _
  private var k: Long = 0
  private var n: Int = 0

  def permute(n0: Int, k0: Long): Array[Int] = {
    n = n0
    k = k0
    fact = new Array[Long](n + 1)
    fact(0) = 1
    var i = 1
    while (i <= n) {
      fact(i) = fact(i - 1) * i
      if (fact(i) > 1e18.toLong) fact(i) = 1e18.toLong + 1
      i += 1
    }
    used = new Array[Boolean](n + 1)
    ans = new java.util.ArrayList[Integer]()
    if (!dfs(0)) return Array.empty[Int]
    Array.tabulate(ans.size())(i => ans.get(i).intValue())
  }

  private def dfs(pos: Int): Boolean = {
    if (pos == n) return true
    var x = 1
    while (x <= n) {
      if (!used(x) && !(pos > 0 && ans.get(pos - 1) % 2 == x % 2)) {
        val rem = n - pos - 1
        val cnt = fact(rem)
        if (cnt >= k) {
          used(x) = true
          ans.add(x)
          if (dfs(pos + 1)) return true
          ans.remove(ans.size() - 1)
          used(x) = false
        } else {
          k -= cnt
        }
      }
      x += 1
    }
    false
  }
}
