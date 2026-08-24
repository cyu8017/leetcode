// LeetCode 0773 - Sliding Puzzle
// https://leetcode.com/problems/sliding-puzzle/

object Solution {
  def slidingPuzzle(board: Array[Array[Int]]): Int = {
    val start = new StringBuilder
    for (row <- board; cell <- row) start.append(cell)
    val target = "123450"
    val neighbors = Array(Array(1, 3), Array(0, 2, 4), Array(1, 5), Array(0, 4), Array(1, 3, 5), Array(2, 4))
    val q = scala.collection.mutable.Queue[(String, Int)]()
    val seen = scala.collection.mutable.HashSet(start.toString)
    q.enqueue((start.toString, 0))
    while (q.nonEmpty) {
      val (state, steps) = q.dequeue()
      if (state == target) return steps
      val zero = state.indexOf('0')
      for (nei <- neighbors(zero)) {
        val nxt = state.toCharArray
        val tmp = nxt(zero)
        nxt(zero) = nxt(nei)
        nxt(nei) = tmp
        val ns = new String(nxt)
        if (seen.add(ns)) q.enqueue((ns, steps + 1))
      }
    }
    -1
  }
}
