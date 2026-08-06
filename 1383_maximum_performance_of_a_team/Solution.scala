object Solution {
  def maxPerformance(n: Int, speed: Array[Int], efficiency: Array[Int], k: Int): Int = {
    val engineers = efficiency.indices.map(i => (efficiency(i), speed(i))).sortBy(-_._1)
    val heap = scala.collection.mutable.PriorityQueue.empty[Int](Ordering.Int.reverse)
    var sum = 0L; var answer = 0L
    engineers.foreach { case (e, s) => heap.enqueue(s); sum += s; if (heap.size > k) sum -= heap.dequeue(); answer = math.max(answer, sum * e) }
    (answer % 1000000007L).toInt
  }
}
