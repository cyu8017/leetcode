// LeetCode 3414 - Maximum Score of Non-overlapping Intervals
// https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/

object Solution {
  private case class It(l: Int, r: Int, w: Int, i: Int)
  private class State(var score: Long = 0, var idx: java.util.ArrayList[Integer] = new java.util.ArrayList[Integer]()) {
    def copy(): State = {
      val s = new State(score)
      s.idx = new java.util.ArrayList[Integer](idx)
      s
    }
  }

  private def better(a: State, b: State): State = {
    if (a.score != b.score) return if (a.score > b.score) a else b
    val n = math.min(a.idx.size, b.idx.size)
    var i = 0
    while (i < n) {
      if (!a.idx.get(i).equals(b.idx.get(i))) return if (a.idx.get(i) < b.idx.get(i)) a else b
      i += 1
    }
    if (a.idx.size <= b.idx.size) a else b
  }

  def maximumWeight(intervals: Array[Array[Int]]): Array[Int] = {
    val n = intervals.length
    val arr = Array.tabulate(n)(i => It(intervals(i)(0), intervals(i)(1), intervals(i)(2), i))
    java.util.Arrays.sort(arr, (a: It, b: It) => java.lang.Integer.compare(a.r, b.r))
    val dp = Array.tabulate(n + 1, 5)((_, _) => new State())
    var i = 1
    var t = 0
    while (i <= n) {
      val cur = arr(i - 1)
      t = 0
      while (t <= 4) {
        dp(i)(t) = dp(i - 1)(t).copy()
        t += 1
      }
      var lo = 0
      var hi = i - 1
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (arr(mid).r < cur.l) lo = mid + 1
        else hi = mid
      }
      val prev = lo
      t = 1
      while (t <= 4) {
        val prevState = dp(prev)(t - 1)
        val cand = prevState.copy()
        cand.score = prevState.score + cur.w
        cand.idx.add(cur.i)
        java.util.Collections.sort(cand.idx)
        dp(i)(t) = better(dp(i)(t), cand)
        t += 1
      }
      i += 1
    }
    var best = dp(n)(0)
    t = 1
    while (t <= 4) {
      best = better(best, dp(n)(t))
      t += 1
    }
    Array.tabulate(best.idx.size)(i => best.idx.get(i).intValue())
  }
}
