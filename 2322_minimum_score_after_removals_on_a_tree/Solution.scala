// LeetCode 2322 - Minimum Score After Removals on a Tree
// https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

object Solution {
  def minimumScore(nums: Array[Int], edges: Array[Array[Int]]): Int = {
    val n = nums.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    val xorv = Array.fill(n)(0)
    val inT = Array.fill(n)(0)
    val outT = Array.fill(n)(0)
    var time = 0

    def dfs(u: Int, p: Int): Unit = {
      inT(u) = time
      time += 1
      xorv(u) = nums(u)
      g(u).foreach { v =>
        if (v != p) {
          dfs(v, u)
          xorv(u) ^= xorv(v)
        }
      }
      outT(u) = time
    }

    def isAncestor(a: Int, b: Int): Boolean = inT(a) <= inT(b) && outT(b) <= outT(a)

    dfs(0, -1)
    val total = xorv(0)
    var ans = Int.MaxValue
    var i = 1
    while (i < n) {
      var j = i + 1
      while (j < n) {
        val (a, b, c) =
          if (isAncestor(i, j)) (xorv(j), xorv(i) ^ xorv(j), total ^ xorv(i))
          else if (isAncestor(j, i)) (xorv(i), xorv(j) ^ xorv(i), total ^ xorv(j))
          else (xorv(i), xorv(j), total ^ xorv(i) ^ xorv(j))
        val mx = math.max(a, math.max(b, c))
        val mn = math.min(a, math.min(b, c))
        ans = math.min(ans, mx - mn)
        j += 1
      }
      i += 1
    }
    ans
  }
}
