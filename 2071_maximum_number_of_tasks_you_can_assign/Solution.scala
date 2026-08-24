// LeetCode 2071 - Maximum Number of Tasks You Can Assign
// https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/

object Solution {
  def maxTaskAssign(tasks: Array[Int], workers: Array[Int], pills: Int, strength: Int): Int = {
    val ts = tasks.sorted
    val wsAll = workers.sorted
    def can(k: Int): Boolean = {
      if (k == 0) return true
      val ws = scala.collection.mutable.TreeMap.empty[Int, Int]
      var i = wsAll.length - k
      while (i < wsAll.length) {
        ws(wsAll(i)) = ws.getOrElse(wsAll(i), 0) + 1
        i += 1
      }
      def remove(x: Int): Unit = {
        val c = ws(x)
        if (c == 1) ws.remove(x)
        else ws(x) = c - 1
      }
      var p = pills
      i = k - 1
      while (i >= 0) {
        val task = ts(i)
        val strongest = ws.lastKey
        if (strongest >= task) remove(strongest)
        else {
          if (p == 0) return false
          val need = task - strength
          val foundOpt = ws.rangeFrom(need).headOption
          if (foundOpt.isEmpty) return false
          remove(foundOpt.get._1)
          p -= 1
        }
        i -= 1
      }
      true
    }
    var lo = 0
    var hi = math.min(ts.length, wsAll.length)
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (can(mid)) lo = mid
      else hi = mid - 1
    }
    lo
  }
}
