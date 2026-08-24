// LeetCode 3715 - Sum of Perfect Square Ancestors
// https://leetcode.com/problems/sum-of-perfect-square-ancestors/

object Solution {
  def sumOfAncestors(n: Int, edges: Array[Array[Int]], nums: Array[Int]): Long = {
    val graph = Array.fill(n)(new java.util.ArrayList[Integer]())
    for (e <- edges) {
      graph(e(0)).add(e(1))
      graph(e(1)).add(e(0))
    }

    def kernel(x0: Int): Int = {
      var x = x0
      var res = 1
      var p = 2
      while (p * p <= x) {
        var cnt = 0
        while (x % p == 0) {
          x /= p
          cnt += 1
        }
        if (cnt % 2 == 1) res *= p
        p += 1
      }
      if (x > 1) res *= x
      res
    }

    val ks = new Array[Int](n)
    var i = 0
    while (i < n) {
      ks(i) = kernel(nums(i))
      i += 1
    }
    val freq = new java.util.HashMap[Integer, Integer]()
    var ans = 0L

    def dfs(u: Int, p: Int): Unit = {
      ans += freq.getOrDefault(ks(u), 0)
      freq.merge(ks(u), 1, Integer.sum)
      val it = graph(u).iterator()
      while (it.hasNext) {
        val v = it.next().intValue()
        if (v != p) dfs(v, u)
      }
      freq.merge(ks(u), -1, Integer.sum)
    }

    dfs(0, -1)
    ans
  }
}
