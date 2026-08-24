// LeetCode 3558 - Number of Ways to Assign Edge Weights I
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

object Solution {
  def dfs(i: Int, fa: Int, g: Array[java.util.ArrayList[Integer]]): Int = {
    var res = 0
    val it = g(i).iterator()
    while (it.hasNext) {
      val j = it.next().intValue()
      if (j != fa) res = math.max(res, dfs(j, i, g) + 1)
    }
    res
  }

  def pow2(exp0: Int, mod: Int): Int = {
    var exp = exp0
    var a = 2L
    var res = 1L
    while (exp > 0) {
      if ((exp & 1) != 0) res = res * a % mod
      a = a * a % mod
      exp >>= 1
    }
    res.toInt
  }

  def assignEdgeWeights(edges: Array[Array[Int]]): Int = {
    val mod = 1000000007
    val n = edges.length + 1
    val g = Array.fill(n + 1)(new java.util.ArrayList[Integer]())
    for (e <- edges) {
      g(e(0)).add(e(1))
      g(e(1)).add(e(0))
    }
    pow2(dfs(1, 0, g) - 1, mod)
  }
}
