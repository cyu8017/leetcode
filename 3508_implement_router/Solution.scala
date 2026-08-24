// LeetCode 3508 - Implement Router
// https://leetcode.com/problems/implement-router/

class Router(_memoryLimit: Int) {
  private val lim: Int = _memoryLimit
  private val vis = new java.util.HashSet[Long]()
  private val q = new java.util.ArrayDeque[Array[Int]]()
  private val idx = scala.collection.mutable.HashMap.empty[Int, Int]
  private val d = scala.collection.mutable.HashMap.empty[Int, java.util.ArrayList[Integer]]

  private def f(a: Int, b: Int, c: Int): Long =
    (a.toLong << 46) | (b.toLong << 29) | c.toLong

  def addPacket(source: Int, destination: Int, timestamp: Int): Boolean = {
    val x = f(source, destination, timestamp)
    if (vis.contains(x)) return false
    vis.add(x)
    if (q.size() >= lim) forwardPacket()
    q.addLast(Array(source, destination, timestamp))
    if (!d.contains(destination)) d(destination) = new java.util.ArrayList[Integer]()
    d(destination).add(timestamp)
    true
  }

  def forwardPacket(): Array[Int] = {
    if (q.isEmpty) return Array.empty[Int]
    val packet = q.pollFirst()
    val s = packet(0)
    val dest = packet(1)
    val t = packet(2)
    vis.remove(f(s, dest, t))
    idx(dest) = idx.getOrElse(dest, 0) + 1
    Array(s, dest, t)
  }

  def getCount(destination: Int, startTime: Int, endTime: Int): Int = {
    val ls = d.getOrElse(destination, null)
    if (ls == null) return 0
    val k = idx.getOrElse(destination, 0)
    lowerBound(ls, k, endTime + 1) - lowerBound(ls, k, startTime)
  }

  private def lowerBound(a: java.util.ArrayList[Integer], from: Int, target: Int): Int = {
    var lo = from
    var hi = a.size()
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a.get(mid) < target) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
