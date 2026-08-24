// LeetCode 3547 - Maximum Sum of Edge Values in a Graph
// https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/

object Solution {
  def calc(left: Int, right: Int, isCycle: Boolean): Long = {
    var w0 = right
    var w1 = right
    var score = 0L
    var value = right - 1
    while (value >= left) {
      score += 1L * w0 * value
      w0 = w1
      w1 = value
      value -= 1
    }
    if (isCycle) score += 1L * w0 * w1
    score
  }

  def getComp(start: Int, graph: Array[java.util.ArrayList[Integer]], seen: Array[Boolean]): java.util.ArrayList[Integer] = {
    val comp = new java.util.ArrayList[Integer]()
    comp.add(start)
    seen(start) = true
    var i = 0
    while (i < comp.size()) {
      val it = graph(comp.get(i)).iterator()
      while (it.hasNext) {
        val v = it.next()
        if (!seen(v)) { seen(v) = true; comp.add(v) }
      }
      i += 1
    }
    comp
  }

  def maxScore(n: Int, edges: Array[Array[Int]]): Long = {
    val graph = Array.fill(n)(new java.util.ArrayList[Integer]())
    for (e <- edges) {
      graph(e(0)).add(e(1))
      graph(e(1)).add(e(0))
    }
    val seen = new Array[Boolean](n)
    val cycleSizes = new java.util.ArrayList[Integer]()
    val pathSizes = new java.util.ArrayList[Integer]()
    var i = 0
    while (i < n) {
      if (!seen(i)) {
        val comp = getComp(i, graph, seen)
        var allDeg2 = true
        val it = comp.iterator()
        while (it.hasNext) {
          val u = it.next()
          if (graph(u).size() != 2) allDeg2 = false
        }
        if (allDeg2) cycleSizes.add(comp.size())
        else if (comp.size() > 1) pathSizes.add(comp.size())
      }
      i += 1
    }
    var ans = 0L
    var curN = n
    val cit = cycleSizes.iterator()
    while (cit.hasNext) {
      val cs = cit.next().intValue()
      ans += calc(curN - cs + 1, curN, true)
      curN -= cs
    }
    pathSizes.sort(java.util.Collections.reverseOrder())
    val pit = pathSizes.iterator()
    while (pit.hasNext) {
      val ps = pit.next().intValue()
      ans += calc(curN - ps + 1, curN, false)
      curN -= ps
    }
    ans
  }
}
