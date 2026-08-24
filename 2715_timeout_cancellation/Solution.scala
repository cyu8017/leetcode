// LeetCode 2715 - Timeout Cancellation
// https://leetcode.com/problems/timeout-cancellation/

object Solution {
  def cancellable(fn: () => Int, t: Int): Array[Any] = {
    var cancelled = false
    val cancel: () => Unit = () => { cancelled = true }
    val result: () => Option[Int] = () => {
      if (cancelled) None
      else Some(fn())
    }
    Array(cancel, result)
  }
}
