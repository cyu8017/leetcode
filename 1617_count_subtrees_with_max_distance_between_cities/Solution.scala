// LeetCode 1617 - Count Subtrees With Max Distance Between Cities
// https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/

object Solution {
  def countSubgraphsForEachDiameter(n: Int, edges: Array[Array[Int]]): Array[Int] = {
    val adj = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- edges) {
      val a = e(0) - 1
      val b = e(1) - 1
      adj(a) += b
      adj(b) += a
    }
    val ans = Array.fill(n - 1)(0)
    def bfs(mask: Int, src: Int): (Int, Map[Int, Int]) = {
      val dist = scala.collection.mutable.Map(src -> 0)
      val q = scala.collection.mutable.Queue(src)
      while (q.nonEmpty) {
        val u = q.dequeue()
        for (v <- adj(u) if ((mask >> v) & 1) == 1 && !dist.contains(v)) {
          dist(v) = dist(u) + 1
          q.enqueue(v)
        }
      }
      val far = dist.maxBy(_._2)._1
      (far, dist.toMap)
    }
    var mask = 1
    while (mask < (1 << n)) {
      if ((mask & (mask - 1)) != 0) {
        val start = Integer.numberOfTrailingZeros(mask)
        val (far, seen) = bfs(mask, start)
        if (seen.size == Integer.bitCount(mask)) {
          val (_, dist) = bfs(mask, far)
          ans(dist.values.max - 1) += 1
        }
      }
      mask += 1
    }
    ans
  }
}
