// LeetCode 1834 - Single-Threaded CPU
// https://leetcode.com/problems/single-threaded-cpu/

object Solution {
  def getOrder(tasks: Array[Array[Int]]): Array[Int] = {
    val indexed = tasks.indices.map(i => (i, tasks(i)(0), tasks(i)(1))).sortBy(t => (t._2, t._1))
    val heap = scala.collection.mutable.PriorityQueue.empty[(Int, Int)](
      Ordering.by[(Int, Int), (Int, Int)](identity).reverse
    )
    var i = 0
    var time = 0L
    val order = scala.collection.mutable.ArrayBuffer.empty[Int]
    val n = tasks.length

    while (i < n || heap.nonEmpty) {
      if (i < n && heap.isEmpty) time = math.max(time, indexed(i)._2.toLong)
      while (i < n && indexed(i)._2 <= time) {
        heap.enqueue((indexed(i)._3, indexed(i)._1))
        i += 1
      }
      val (duration, idx) = heap.dequeue()
      time += duration
      order += idx
    }
    order.toArray
  }
}
