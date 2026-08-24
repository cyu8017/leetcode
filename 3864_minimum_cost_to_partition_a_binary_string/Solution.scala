// LeetCode 3864 - Minimum Cost To Partition A Binary String
// https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/

object Solution {
  private var pre: Array[Int] = _
  private var encCost: Int = _
  private var flatCost: Int = _

  def minCost(s: String, encCost: Int, flatCost: Int): Long = {
    val n = s.length
    this.encCost = encCost
    this.flatCost = flatCost
    pre = new Array[Int](n + 1)
    var i = 1
    while (i <= n) {
      pre(i) = pre(i - 1) + (s.charAt(i - 1) - '0')
      i += 1
    }
    dfs(0, n)
  }

  private def dfs(l: Int, r: Int): Long = {
    val x = pre(r) - pre(l)
    var res = if (x != 0) (r - l).toLong * x * encCost else flatCost.toLong
    if ((r - l) % 2 == 0) {
      val m = (l + r) / 2
      res = math.min(res, dfs(l, m) + dfs(m, r))
    }
    res
  }
}
