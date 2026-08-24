// LeetCode 2479 - Maximum XOR of Two Non-Overlapping Subtrees
// https://leetcode.com/problems/maximum-xor-of-two-non-overlapping-subtrees/

object Solution {
  private class Trie {
    val child = Array.fill[Trie](2)(null)
  }

  def maxXor(n: Int, edges: Array[Array[Int]], values: Array[Int]): Long = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    val sum = new Array[Long](n)

    def dfsSum(u: Int, p: Int): Long = {
      var s = values(u).toLong
      g(u).foreach { v => if (v != p) s += dfsSum(v, u) }
      sum(u) = s
      s
    }

    val root = new Trie()
    var ans = 0L

    def insert(x: Long): Unit = {
      var cur = root
      var b = 46
      while (b >= 0) {
        val bit = ((x >> b) & 1).toInt
        if (cur.child(bit) == null) cur.child(bit) = new Trie()
        cur = cur.child(bit)
        b -= 1
      }
    }

    def query(x: Long): Long = {
      var cur = root
      if (cur.child(0) == null && cur.child(1) == null) return 0L
      var res = 0L
      var b = 46
      while (b >= 0) {
        val bit = ((x >> b) & 1).toInt
        val want = bit ^ 1
        if (cur.child(want) != null) {
          res |= 1L << b
          cur = cur.child(want)
        } else if (cur.child(bit) != null) {
          cur = cur.child(bit)
        } else {
          return res
        }
        b -= 1
      }
      res
    }

    def dfs(u: Int, p: Int): Unit = {
      g(u).foreach { v =>
        if (v != p) {
          val xorv = query(sum(v))
          if (xorv > ans) ans = xorv
          dfs(v, u)
          insert(sum(v))
        }
      }
    }

    dfsSum(0, -1)
    dfs(0, -1)
    ans
  }
}
