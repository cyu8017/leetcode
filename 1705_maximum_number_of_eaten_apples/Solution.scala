// LeetCode 1705 - Maximum Number of Eaten Apples
// https://leetcode.com/problems/maximum-number-of-eaten-apples/

object Solution {
  def eatenApples(apples: Array[Int], days: Array[Int]): Int = {
    val heap = scala.collection.mutable.PriorityQueue.empty[(Int, Int)](
      Ordering.by[(Int, Int), Int](-_._1)
    )
    val n = apples.length
    var day = 0
    var eaten = 0
    while (day < n || heap.nonEmpty) {
      if (day < n && apples(day) > 0) {
        heap.enqueue((day + days(day), apples(day)))
      }
      while (heap.nonEmpty && heap.head._1 <= day) {
        heap.dequeue()
      }
      if (heap.nonEmpty) {
        val (expire, count) = heap.dequeue()
        eaten += 1
        if (count > 1) {
          heap.enqueue((expire, count - 1))
        }
      }
      day += 1
    }
    eaten
  }
}
