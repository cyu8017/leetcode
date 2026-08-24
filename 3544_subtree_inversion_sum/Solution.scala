// LeetCode 3544 - Subtree Inversion Sum
// https://leetcode.com/problems/subtree-inversion-sum/

object Solution {
  def subtreeInversionSum(edges: Array[Array[Int]], nums: Array[Int], k: Int): Long = {
    val n = edges.length + 1
    val graph = Array.fill(n)(new java.util.ArrayList[Integer]())
    for (e <- edges) {
      graph(e(0)).add(e(1))
      graph(e(1)).add(e(0))
    }
    val parent = Array.fill(n)(-1)
    val memo = scala.collection.mutable.HashMap.empty[String, Long]

    def dp(u: Int, steps: Int, inv: Boolean): Long = {
      val key = u + "," + steps + "," + inv
      if (memo.contains(key)) return memo(key)
      var num = nums(u).toLong
      if (inv) num = -num
      var negNum = -num
      val it = graph(u).iterator()
      while (it.hasNext) {
        val v = it.next().intValue()
        if (v != parent(u)) {
          parent(v) = u
          var ns = steps + 1
          if (ns > k) ns = k
          num += dp(v, ns, inv)
          if (steps == k) negNum += dp(v, 1, !inv)
        }
      }
      var res = num
      if (steps == k && negNum > res) res = negNum
      memo(key) = res
      res
    }

    dp(0, k, false)
  }
}
