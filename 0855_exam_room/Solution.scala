// LeetCode 0855 - Exam Room
// https://leetcode.com/problems/exam-room/

class ExamRoom(_n: Int) {
  private val n = _n
  private val seats = scala.collection.mutable.TreeSet.empty[Int]

  def seat(): Int = {
    if (seats.isEmpty) {
      seats += 0
      return 0
    }
    var bestSeat = 0
    var bestDist = seats.head
    var prev = seats.head
    seats.foreach { cur =>
      if (cur != prev) {
        val dist = (cur - prev) / 2
        if (dist > bestDist) {
          bestDist = dist
          bestSeat = prev + dist
        }
        prev = cur
      }
    }
    if (n - 1 - seats.last > bestDist) bestSeat = n - 1
    seats += bestSeat
    bestSeat
  }

  def leave(p: Int): Unit = {
    seats -= p
  }
}
