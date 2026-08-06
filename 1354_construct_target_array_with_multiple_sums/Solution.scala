import java.util.PriorityQueue

object Solution {
  def isPossible(target: Array[Int]): Boolean = {
    if (target.length == 1) return target(0) == 1
    val pq = new PriorityQueue[Long](java.util.Collections.reverseOrder()); var total = 0L
    target.foreach(x => { total += x; pq.offer(x.toLong) })
    while (true) {
      val x = pq.poll(); val rest = total - x
      if (x == 1 || rest == 1) return true
      if (rest == 0 || x <= rest) return false
      val previous = x % rest
      if (previous == 0) return false
      total = rest + previous; pq.offer(previous)
    }
    false
  }
}
