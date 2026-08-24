// LeetCode 3910 - Count Connected Subgraphs With Even Node Sum
// https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/

object Solution {
  private var g: Array[scala.collection.mutable.ArrayBuffer[Int]] = _
  private var vis: Int = _
  private var m: Int = _

  def evenSumSubgraphs(nums: Array[Int], edges: Array[Array[Int]]): Int = {
    val n = nums.length
    g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    m = (1 << n) - 1
    var ans = 0
    var sub = 1
    while (sub <= m) {
      var s = 0
      var i = 0
      while (i < n) {
        if (((sub >> i) & 1) != 0) s += nums(i)
        i += 1
      }
      if (s % 2 == 0) {
        vis = m ^ sub
        val start = 31 - Integer.numberOfLeadingZeros(sub)
        dfs(start)
        if (vis == m) ans += 1
      }
      sub += 1
    }
    ans
  }

  private def dfs(u: Int): Unit = {
    vis |= 1 << u
    g(u).foreach { v =>
      if (((vis >> v) & 1) == 0) dfs(v)
    }
  }
}
