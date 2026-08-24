// LeetCode 2350 - Shortest Impossible Sequence of Rolls
// https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/

object Solution {
  def shortestSequence(rolls: Array[Int], k: Int): Int = {
    val seen = scala.collection.mutable.HashSet.empty[Int]
    var ans = 1
    rolls.foreach { r =>
      seen += r
      if (seen.size == k) {
        ans += 1
        seen.clear()
      }
    }
    ans
  }
}
