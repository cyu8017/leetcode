// LeetCode 0752 - Open the Lock
// https://leetcode.com/problems/open-the-lock/

object Solution {
  def openLock(deadends: Array[String], target: String): Int = {
    val dead = deadends.toSet
    if (dead.contains("0000")) return -1
    val q = scala.collection.mutable.Queue[(String, Int)]()
    val seen = scala.collection.mutable.HashSet("0000")
    q.enqueue(("0000", 0))
    while (q.nonEmpty) {
      val (state, steps) = q.dequeue()
      if (state == target) return steps
      val chars = state.toCharArray
      var i = 0
      while (i < 4) {
        val digit = chars(i) - '0'
        for (delta <- Array(-1, 1)) {
          chars(i) = ('0' + (digit + delta + 10) % 10).toChar
          val nxt = new String(chars)
          chars(i) = ('0' + digit).toChar
          if (seen.add(nxt) && !dead.contains(nxt)) q.enqueue((nxt, steps + 1))
        }
        i += 1
      }
    }
    -1
  }
}
