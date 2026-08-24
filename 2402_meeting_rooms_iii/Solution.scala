// LeetCode 2402 - Meeting Rooms III
// https://leetcode.com/problems/meeting-rooms-iii/

object Solution {
  def mostBooked(n: Int, meetings: Array[Array[Int]]): Int = {
    scala.util.Sorting.stableSort(meetings, (a: Array[Int], b: Array[Int]) => a(0) < b(0))
    val free = scala.collection.mutable.PriorityQueue.empty[Long](Ordering[Long].reverse)
    var i = 0
    while (i < n) {
      free.enqueue(i.toLong)
      i += 1
    }
    val busy = scala.collection.mutable.PriorityQueue.empty[(Long, Long)](
      Ordering.Tuple2[Long, Long].reverse
    )
    val cnt = Array.fill(n)(0)
    meetings.foreach { m =>
      val start = m(0).toLong
      val end = m(1).toLong
      while (busy.nonEmpty && busy.head._1 <= start) {
        free.enqueue(busy.dequeue()._2)
      }
      val dur = end - start
      val (begin, room) =
        if (free.nonEmpty) (start, free.dequeue())
        else {
          val top = busy.dequeue()
          (top._1, top._2)
        }
      busy.enqueue((begin + dur, room))
      cnt(room.toInt) += 1
    }
    var ans = 0
    i = 1
    while (i < n) {
      if (cnt(i) > cnt(ans)) ans = i
      i += 1
    }
    ans
  }
}
