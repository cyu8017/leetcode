// LeetCode 2725 - Interval Cancellation
// https://leetcode.com/problems/interval-cancellation/

object Solution {
  def cancellable(fn: () => Int, t: Int, times: Int): Array[Any] = {
    var cancelled = false
    val results = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < times && !cancelled) {
      results += fn()
      i += 1
    }
    val cancel: () => Unit = () => { cancelled = true }
    Array(cancel, results.toArray)
  }
}
