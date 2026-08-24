// LeetCode 0767 - Reorganize String
// https://leetcode.com/problems/reorganize-string/

object Solution {
  def reorganizeString(s: String): String = {
    val freq = Array.fill(26)(0)
    for (ch <- s) freq(ch - 'a') += 1
    val heap = scala.collection.mutable.PriorityQueue.empty[(Int, Int)]
    var i = 0
    while (i < 26) {
      if (freq(i) > 0) heap.enqueue((freq(i), i))
      i += 1
    }
    if (heap.nonEmpty && heap.head._1 > (s.length + 1) / 2) return ""
    val result = new StringBuilder
    while (heap.size >= 2) {
      val x = heap.dequeue()
      val y = heap.dequeue()
      result.append(('a' + x._2).toChar)
      result.append(('a' + y._2).toChar)
      if (x._1 - 1 > 0) heap.enqueue((x._1 - 1, x._2))
      if (y._1 - 1 > 0) heap.enqueue((y._1 - 1, y._2))
    }
    if (heap.nonEmpty) result.append(('a' + heap.head._2).toChar)
    result.toString
  }
}
