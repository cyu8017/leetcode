// LeetCode 2059 - Minimum Operations to Convert Number
// https://leetcode.com/problems/minimum-operations-to-convert-number/

object Solution {
  def minimumOperations(nums: Array[Int], start: Int, goal: Int): Int = {
    if (start == goal) return 0
    val vis = scala.collection.mutable.HashSet(start)
    val q = scala.collection.mutable.Queue(start)
    var steps = 0
    while (q.nonEmpty) {
      steps += 1
      val sz = q.size
      var s = 0
      while (s < sz) {
        val cur = q.dequeue()
        nums.foreach { x =>
          Array(cur + x, cur - x, cur ^ x).foreach { nxt =>
            if (nxt == goal) return steps
            if (nxt >= 0 && nxt <= 1000 && vis.add(nxt)) q.enqueue(nxt)
          }
        }
        s += 1
      }
    }
    -1
  }
}
