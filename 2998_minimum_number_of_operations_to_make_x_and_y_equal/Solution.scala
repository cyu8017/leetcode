// LeetCode 2998 - Minimum Number of Operations to Make X and Y Equal
// https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/

object Solution {
  def minimumOperationsToMakeEqual(x: Int, y: Int): Int = {
    if (x <= y) return y - x
    val q = scala.collection.mutable.Queue[(Int, Int)]()
    q.enqueue((x, 0))
    val seen = scala.collection.mutable.HashSet[Int](x)
    while (q.nonEmpty) {
      val (v, d) = q.dequeue()
      if (v == y) return d
      val cands = Array(v + 1, v - 1, if (v % 11 == 0) v / 11 else -1, if (v % 5 == 0) v / 5 else -1)
      for (nxt <- cands) {
        if (nxt > 0 && nxt < 2 * x + 20 && seen.add(nxt)) q.enqueue((nxt, d + 1))
      }
    }
    -1
  }
}
