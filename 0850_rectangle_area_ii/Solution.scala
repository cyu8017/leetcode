// LeetCode 0850 - Rectangle Area II
// https://leetcode.com/problems/rectangle-area-ii/

object Solution {
  def rectangleArea(rectangles: Array[Array[Int]]): Int = {
    val MOD = 1000000007
    val events = scala.collection.mutable.ListBuffer.empty[Array[Int]]
    rectangles.foreach { r =>
      events += Array(r(0), 1, r(1), r(3))
      events += Array(r(2), -1, r(1), r(3))
    }
    val ev = events.toArray
    scala.util.Sorting.quickSort(ev)(Ordering.by(_(0)))
    def coveredLength(active: List[Array[Int]]): Int = {
      if (active.isEmpty) return 0
      val sorted = active.sortBy(_(0))
      var total = 0
      var curStart = sorted.head(0)
      var curEnd = sorted.head(1)
      sorted.tail.foreach { iv =>
        val start = iv(0)
        val end = iv(1)
        if (start > curEnd) {
          total += curEnd - curStart
          curStart = start
          curEnd = end
        } else curEnd = math.max(curEnd, end)
      }
      total + curEnd - curStart
    }
    var active = List.empty[Array[Int]]
    var area = 0L
    var prevX = ev(0)(0)
    ev.foreach { e =>
      val x = e(0)
      val typ = e(1)
      val y1 = e(2)
      val y2 = e(3)
      area += coveredLength(active).toLong * (x - prevX)
      if (typ == 1) active = active :+ Array(y1, y2)
      else {
        val idx = active.indexWhere(a => a(0) == y1 && a(1) == y2)
        if (idx >= 0) active = active.patch(idx, Nil, 1)
      }
      prevX = x
    }
    (area % MOD).toInt
  }
}
