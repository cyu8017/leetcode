// LeetCode 2581 - Count Number of Possible Root Nodes
// https://leetcode.com/problems/count-number-of-possible-root-nodes/

object Solution {
  def rootCount(edges: Array[Array[Int]], guesses: Array[Array[Int]], k: Int): Int = {
    val n = edges.length + 1
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    val guessSet = scala.collection.mutable.Set.empty[Long]
    def pack(a: Int, b: Int): Long = (a.toLong << 32) | (b & 0xffffffffL)
    guesses.foreach(gu => guessSet += pack(gu(0), gu(1)))
    var ans = 0
    def dfs1(u: Int, p: Int): Int = {
      var cnt = 0
      g(u).foreach { v =>
        if (v != p) {
          if (guessSet.contains(pack(u, v))) cnt += 1
          cnt += dfs1(v, u)
        }
      }
      cnt
    }
    def dfs2(u: Int, p: Int, cur: Int): Unit = {
      if (cur >= k) ans += 1
      g(u).foreach { v =>
        if (v != p) {
          var nxt = cur
          if (guessSet.contains(pack(u, v))) nxt -= 1
          if (guessSet.contains(pack(v, u))) nxt += 1
          dfs2(v, u, nxt)
        }
      }
    }
    val baseCnt = dfs1(0, -1)
    dfs2(0, -1, baseCnt)
    ans
  }
}
