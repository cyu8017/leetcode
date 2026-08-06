// LeetCode 1938 - Maximum Genetic Difference Query
// https://leetcode.com/problems/maximum-genetic-difference-query/

object Solution {
  private class TrieNode {
    val child = Array.fill[TrieNode](2)(null)
    var cnt = 0
  }

  def maxGeneticDifference(parents: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val n = parents.length
    val children = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    var root = 0
    for (i <- parents.indices) {
      if (parents(i) == -1) root = i
      else children(parents(i)) += i
    }
    val qmap = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[(Int, Int)])
    for (i <- queries.indices) qmap(queries(i)(0)) += ((i, queries(i)(1)))
    val ans = Array.ofDim[Int](queries.length)
    val trieRoot = new TrieNode
    val BITS = 17

    def trieUpdate(num: Int, delta: Int): Unit = {
      var node = trieRoot
      for (b <- BITS to 0 by -1) {
        val bit = (num >> b) & 1
        if (node.child(bit) == null) node.child(bit) = new TrieNode
        node = node.child(bit)
        node.cnt += delta
      }
    }

    def trieMaxXor(num: Int): Int = {
      var node = trieRoot
      var res = 0
      for (b <- BITS to 0 by -1) {
        val bit = (num >> b) & 1
        val want = 1 - bit
        if (node.child(want) != null && node.child(want).cnt > 0) {
          res |= 1 << b
          node = node.child(want)
        } else {
          node = node.child(bit)
        }
      }
      res
    }

    def dfs(u: Int): Unit = {
      trieUpdate(u, 1)
      for ((qi, valu) <- qmap(u)) ans(qi) = trieMaxXor(valu)
      for (v <- children(u)) dfs(v)
      trieUpdate(u, -1)
    }

    dfs(root)
    ans
  }
}
