// LeetCode 1215 - Stepping Numbers
// https://leetcode.com/problems/stepping-numbers/

object Solution {
  def countSteppingNumbers(low: Int, high: Int): List[Int] = {
    val answer = scala.collection.mutable.ListBuffer.empty[Int]
    if (low == 0) answer += 0
    val q = scala.collection.mutable.Queue((1 to 9): _*)
    while (q.nonEmpty) {
      val x = q.dequeue()
      if (x <= high) {
        if (x >= low) answer += x
        val last = x % 10
        if (last > 0) {
          val next = x * 10L + last - 1
          if (next <= high) q.enqueue(next.toInt)
        }
        if (last < 9) {
          val next = x * 10L + last + 1
          if (next <= high) q.enqueue(next.toInt)
        }
      }
    }
    answer.toList.sorted
  }
}
