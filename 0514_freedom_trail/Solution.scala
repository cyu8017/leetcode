// LeetCode 0514 - Freedom Trail
// https://leetcode.com/problems/freedom-trail/

import scala.collection.mutable

object Solution {
  def findRotateSteps(ring: String, key: String): Int = {
    val positions = mutable.Map[Char, mutable.ArrayBuffer[Int]]()
    for (index <- ring.indices) {
      positions.getOrElseUpdate(ring(index), mutable.ArrayBuffer.empty). += index
    }
    val memo = mutable.Map[(Int, Int), Int]()

    def dp(ringIndex: Int, keyIndex: Int): Int = {
      if (keyIndex == key.length) {
        return 0
      }
      val state = (ringIndex, keyIndex)
      memo.get(state) match {
        case Some(value) => value
        case None =>
          var best = Int.MaxValue
          for (pos <- positions(key(keyIndex))) {
            val clockwise = (pos - ringIndex + ring.length) % ring.length
            val counter = (ringIndex - pos + ring.length) % ring.length
            val steps = math.min(clockwise, counter) + 1
            best = math.min(best, steps + dp(pos, keyIndex + 1))
          }
          memo(state) = best
          best
      }
    }

    dp(0, 0)
  }
}
