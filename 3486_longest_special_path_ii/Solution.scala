// LeetCode 3486 - Longest Special Path II
// https://leetcode.com/problems/longest-special-path-ii/

object Solution {
  private var g: Array[java.util.ArrayList[Array[Int]]] = _
  private var nums: Array[Int] = _
  private var bestLen = 0
  private var bestNodes = 0

  def longestSpecialPath(edges: Array[Array[Int]], nums0: Array[Int]): Array[Int] = {
    nums = nums0
    val n = nums.length
    g = Array.fill(n)(new java.util.ArrayList[Array[Int]]())
    edges.foreach { e =>
      g(e(0)).add(Array(e(1), e(2)))
      g(e(1)).add(Array(e(0), e(2)))
    }
    bestLen = 0
    bestNodes = 1
    dfs(0, -1, 0, new java.util.ArrayList[Integer](), new java.util.ArrayList[Integer]())
    Array(bestLen, bestNodes)
  }

  private def dfs(u: Int, p: Int, dist: Int, pathVals: java.util.ArrayList[Integer], pathDist: java.util.ArrayList[Integer]): Unit = {
    pathVals.add(nums(u))
    pathDist.add(dist)
    val freq = new java.util.HashMap[Integer, Integer]()
    var dups = 0
    var left = 0
    var right = 0
    while (right < pathVals.size()) {
      val v = pathVals.get(right)
      freq.put(v, freq.getOrDefault(v, 0) + 1)
      if (freq.get(v) == 2) dups += 1
      while (dups > 1) {
        val lv = pathVals.get(left)
        if (freq.get(lv) == 2) dups -= 1
        freq.put(lv, freq.get(lv) - 1)
        left += 1
      }
      right += 1
    }
    val length = dist - pathDist.get(left)
    val nodes = pathVals.size() - left
    if (length > bestLen || (length == bestLen && nodes < bestNodes)) {
      bestLen = length
      bestNodes = nodes
    }
    val it = g(u).iterator()
    while (it.hasNext) {
      val e = it.next()
      if (e(0) != p) dfs(e(0), u, dist + e(1), pathVals, pathDist)
    }
    pathVals.remove(pathVals.size() - 1)
    pathDist.remove(pathDist.size() - 1)
  }
}
