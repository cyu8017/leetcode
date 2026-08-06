import java.util.PriorityQueue

object Solution {
  def maxEvents(events: Array[Array[Int]]): Int = {
    val sorted = events.sortBy(_(0)); val pq = new PriorityQueue[Int]()
    var i = 0; var day = 0; var answer = 0
    while (i < sorted.length || !pq.isEmpty) {
      if (pq.isEmpty) day = math.max(day, sorted(i)(0))
      while (i < sorted.length && sorted(i)(0) <= day) { pq.offer(sorted(i)(1)); i += 1 }
      while (!pq.isEmpty && pq.peek < day) pq.poll()
      if (!pq.isEmpty) { pq.poll(); answer += 1; day += 1 }
    }
    answer
  }
}
