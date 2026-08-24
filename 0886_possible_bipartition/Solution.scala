// LeetCode 0886 - Possible Bipartition
// https://leetcode.com/problems/possible-bipartition/

object Solution {
  def possibleBipartition(n: Int, dislikes: Array[Array[Int]]): Boolean = {
    val graph = Array.fill(n + 1)(scala.collection.mutable.ArrayBuffer.empty[Int])
    dislikes.foreach { e =>
      graph(e(0)) += e(1)
      graph(e(1)) += e(0)
    }
    val color = scala.collection.mutable.Map.empty[Int, Int]
    var start = 1
    while (start <= n) {
      if (!color.contains(start)) {
        val queue = scala.collection.mutable.Queue[Int]()
        queue.enqueue(start)
        color(start) = 0
        while (queue.nonEmpty) {
          val node = queue.dequeue()
          graph(node).foreach { nei =>
            if (!color.contains(nei)) {
              color(nei) = color(node) ^ 1
              queue.enqueue(nei)
            } else if (color(nei) == color(node)) return false
          }
        }
      }
      start += 1
    }
    true
  }
}
