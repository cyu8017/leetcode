// LeetCode 2368 - Reachable Nodes With Restrictions
// https://leetcode.com/problems/reachable-nodes-with-restrictions/

object Solution {
  def reachableNodes(n: Int, edges: Array[Array[Int]], restricted: Array[Int]): Int = {
    val ban = scala.collection.mutable.HashSet.empty[Int]
    restricted.foreach(x => ban += x)
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    var ans = 0
    val vis = Array.fill(n)(false)
    val q = scala.collection.mutable.Queue.empty[Int]
    q.enqueue(0)
    vis(0) = true
    while (q.nonEmpty) {
      val u = q.dequeue()
      ans += 1
      g(u).foreach { v =>
        if (!vis(v) && !ban.contains(v)) {
          vis(v) = true
          q.enqueue(v)
        }
      }
    }
    ans
  }
}
