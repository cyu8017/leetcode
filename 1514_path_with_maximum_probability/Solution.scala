// LeetCode 1514 - Path with Maximum Probability
// https://leetcode.com/problems/path-with-maximum-probability/

object Solution {
  def maxProbability(n: Int, edges: Array[Array[Int]], succProb: Array[Double], start_node: Int, end_node: Int): Double = {
    val graph = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[(Int, Double)])
    for (i <- edges.indices) {
      val Array(a, b) = edges(i)
      val p = succProb(i)
      graph(a) += ((b, p))
      graph(b) += ((a, p))
    }
    val best = Array.fill(n)(0.0)
    best(start_node) = 1.0
    val pq = scala.collection.mutable.PriorityQueue.empty[(Double, Int)]
    pq.enqueue((1.0, start_node))
    while (pq.nonEmpty) {
      val (prob, node) = pq.dequeue()
      if (node == end_node) return prob
      if (prob >= best(node) - 1e-15) {
        for ((nei, ep) <- graph(node)) {
          val cand = prob * ep
          if (cand > best(nei)) {
            best(nei) = cand
            pq.enqueue((cand, nei))
          }
        }
      }
    }
    0.0
  }
}
