// LeetCode 3709 - Design Exam Scores Tracker
// https://leetcode.com/problems/design-exam-scores-tracker/

class ExamTracker() {
  private val times = new java.util.ArrayList[Integer]()
  private val pre = new java.util.ArrayList[java.lang.Long]()
  times.add(0)
  pre.add(0L)

  def record(time: Int, score: Int): Unit = {
    times.add(time)
    pre.add(pre.get(pre.size() - 1) + score)
  }

  def totalScore(startTime: Int, endTime: Int): Long = {
    val l = ExamTracker.lowerBound(times, startTime) - 1
    val r = ExamTracker.lowerBound(times, endTime + 1) - 1
    pre.get(r) - pre.get(l)
  }
}

object ExamTracker {
  private def lowerBound(a: java.util.List[Integer], target: Int): Int = {
    var lo = 0
    var hi = a.size()
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a.get(mid) < target) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
