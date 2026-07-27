// LeetCode 1654 - Minimum Jumps to Reach Home
// https://leetcode.com/problems/minimum-jumps-to-reach-home/

object Solution {
  def minimumJumps(forbidden: Array[Int], a: Int, b: Int, x: Int): Int = {
    val bad = forbidden.toSet
    var limit = x
    for (f <- forbidden) if (f > limit) limit = f
    limit += a + b

    case class State(pos: Int, back: Boolean)
    case class Item(pos: Int, dist: Int, back: Boolean)
    val q = scala.collection.mutable.Queue[Item](Item(0, 0, false))
    val seen = scala.collection.mutable.Set[State](State(0, false))

    while (q.nonEmpty) {
      val cur = q.dequeue()
      if (cur.pos == x) return cur.dist
      val candidates = scala.collection.mutable.ArrayBuffer((cur.pos + a, false))
      if (!cur.back) candidates += ((cur.pos - b, true))
      for ((np, back) <- candidates) {
        if (np >= 0 && np <= limit && !bad.contains(np)) {
          val st = State(np, back)
          if (!seen.contains(st)) {
            seen += st
            q.enqueue(Item(np, cur.dist + 1, back))
          }
        }
      }
    }
    -1
  }
}
