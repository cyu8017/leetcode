// LeetCode 1723 - Find Minimum Time to Finish All Jobs
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/

object Solution {
  def minimumTimeRequired(jobs: Array[Int], k: Int): Int = {
    val sorted = jobs.sorted(Ordering[Int].reverse)
    val loads = new Array[Int](k)
    var best = sorted.sum

    def backtrack(i: Int): Unit = {
      if (i == sorted.length) {
        best = math.min(best, loads.max)
        return
      }
      val seen = scala.collection.mutable.Set.empty[Int]
      var worker = 0
      var stop = false
      while (worker < k && !stop) {
        if (!seen.contains(loads(worker)) && loads(worker) + sorted(i) < best) {
          seen.add(loads(worker))
          loads(worker) += sorted(i)
          backtrack(i + 1)
          loads(worker) -= sorted(i)
          if (loads(worker) == 0) {
            stop = true
          }
        }
        worker += 1
      }
    }

    backtrack(0)
    best
  }
}
