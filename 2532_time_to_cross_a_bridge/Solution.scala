// LeetCode 2532 - Time to Cross a Bridge
// https://leetcode.com/problems/time-to-cross-a-bridge/

object Solution {
  private class Worker(val idx: Int, t: Array[Int]) {
    val leftToRight: Int = t(0)
    val pickOld: Int = t(1)
    val rightToLeft: Int = t(2)
    val putNew: Int = t(3)
    val efficiency: Int = t(0) + t(2)
  }

  def findCrossingTime(n: Int, k: Int, time: Array[Array[Int]]): Int = {
    val ord: Ordering[Worker] = Ordering.fromLessThan { (a, b) =>
      if (a.efficiency != b.efficiency) a.efficiency < b.efficiency
      else a.idx < b.idx
    }
    val left = scala.collection.mutable.PriorityQueue.empty[Worker](ord)
    val right = scala.collection.mutable.PriorityQueue.empty[Worker](ord)
    val ws = Array.ofDim[Worker](k)
    var i = 0
    while (i < k) {
      ws(i) = new Worker(i, time(i))
      left.enqueue(ws(i))
      i += 1
    }
    val events = scala.collection.mutable.PriorityQueue.empty[Array[Long]](
      Ordering.by[Array[Long], Long](_(0)).reverse
    )
    var cur = 0L
    var bridgeFree = 0L
    var remain = n
    var done = 0
    while (done < n) {
      while (events.nonEmpty && events.head(0) <= cur) {
        val e = events.dequeue()
        val w = ws(e(2).toInt)
        if (e(1).toInt == 0) left.enqueue(w)
        else right.enqueue(w)
      }
      if (cur < bridgeFree) {
        cur = bridgeFree
      } else if (right.nonEmpty) {
        val w = right.dequeue()
        cur += w.rightToLeft
        bridgeFree = cur
        events.enqueue(Array(cur + w.putNew, 0, w.idx.toLong))
        done += 1
      } else if (left.nonEmpty && remain > 0) {
        val w = left.dequeue()
        cur += w.leftToRight
        bridgeFree = cur
        remain -= 1
        events.enqueue(Array(cur + w.pickOld, 1, w.idx.toLong))
      } else if (events.isEmpty) {
        return cur.toInt
      } else {
        cur = events.head(0)
      }
    }
    cur.toInt
  }
}
