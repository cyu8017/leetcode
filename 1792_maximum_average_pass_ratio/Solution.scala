// LeetCode 1792 - Maximum Average Pass Ratio
// https://leetcode.com/problems/maximum-average-pass-ratio/

object Solution {
  def maxAverageRatio(classes: Array[Array[Int]], extraStudents: Int): Double = {
    def gain(p: Double, t: Double): Double = (p + 1) / (t + 1) - p / t

    val heap = scala.collection.mutable.PriorityQueue.empty[(Double, Double, Double)](
      Ordering.by(_._1)
    )
    for (cls <- classes) {
      val p = cls(0).toDouble
      val t = cls(1).toDouble
      heap.enqueue((gain(p, t), p, t))
    }
    for (_ <- 0 until extraStudents) {
      val (_, p0, t0) = heap.dequeue()
      val p = p0 + 1
      val t = t0 + 1
      heap.enqueue((gain(p, t), p, t))
    }
    heap.iterator.map { case (_, p, t) => p / t }.sum / classes.length
  }
}
