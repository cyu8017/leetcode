// LeetCode 3425 - Longest Special Path
// https://leetcode.com/problems/longest-special-path/

object Solution {
  private var g: Array[java.util.ArrayList[Array[Int]]] = _
  private var nums: Array[Int] = _
  private var bestLen = 0
  private var bestNodes = 0
  private val last = new java.util.HashMap[Integer, Integer]()

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
    last.clear()
    val path = new java.util.ArrayList[Integer]()
    dfs(0, -1, 0, 0, path)
    Array(bestLen, bestNodes)
  }

  private def dfs(u: Int, p: Int, dist: Int, left: Int, path: java.util.ArrayList[Integer]): Unit = {
    var prevPos = -1
    val seen = last.containsKey(nums(u))
    if (seen) prevPos = last.get(nums(u))
    last.put(nums(u), path.size())
    var newLeft = left
    if (seen && prevPos >= left) newLeft = prevPos + 1
    path.add(dist)
    val length = dist - path.get(newLeft)
    val nodes = path.size() - newLeft
    if (length > bestLen || (length == bestLen && nodes < bestNodes)) {
      bestLen = length
      bestNodes = nodes
    }
    val it = g(u).iterator()
    while (it.hasNext) {
      val e = it.next()
      if (e(0) != p) dfs(e(0), u, dist + e(1), newLeft, path)
    }
    path.remove(path.size() - 1)
    if (seen) last.put(nums(u), prevPos)
    else last.remove(nums(u))
  }
}
