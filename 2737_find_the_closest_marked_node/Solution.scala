// LeetCode 2737 - Find the Closest Marked Node
// https://leetcode.com/problems/find-the-closest-marked-node/

object Solution {
  def minimumDistance(n: Int, edges: Array[Array[Int]], s: Int, marked: Array[Int]): Int = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[(Int, Int)])
    edges.foreach(e => g(e(0)) += ((e(1), e(2))))
    val mark = marked.toSet
    val dist = Array.fill(n)(Int.MaxValue / 4)
    dist(s) = 0
    val pq = scala.collection.mutable.PriorityQueue.empty[(Int, Int)](Ordering.by[(Int, Int), Int](_._1).reverse)
    pq.enqueue((0, s))
    while (pq.nonEmpty) {
      val (d, u) = pq.dequeue()
      if (mark.contains(u)) return d
      if (d <= dist(u)) {
        g(u).foreach { case (v, w) =>
          if (d + w < dist(v)) {
            dist(v) = d + w
            pq.enqueue((dist(v), v))
          }
        }
      }
    }
    -1
  }
}
