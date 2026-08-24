// LeetCode 0857 - Minimum Cost to Hire K Workers
// https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

object Solution {
  def mincostToHireWorkers(quality: Array[Int], wage: Array[Int], k: Int): Double = {
    val n = quality.length
    val workers = Array.tabulate(n)(i => (wage(i).toDouble / quality(i), quality(i)))
    scala.util.Sorting.quickSort(workers)(Ordering.by(_._1))
    val heap = scala.collection.mutable.PriorityQueue.empty[Int]
    var totalQ = 0L
    var ans = 1e18
    workers.foreach { case (ratio, q) =>
      heap.enqueue(q)
      totalQ += q
      if (heap.size > k) totalQ -= heap.dequeue()
      if (heap.size == k) ans = math.min(ans, totalQ * ratio)
    }
    ans
  }
}
