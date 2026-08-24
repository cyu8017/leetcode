// LeetCode 2650 - Design Cancellable Function
// https://leetcode.com/problems/design-cancellable-function/

object Solution {
  def cancellable(generator: () => Int): Array[Any] = {
    var cancelled = false
    var done = false
    var result = 0
    val cancel: () => Unit = () => { cancelled = true }
    val run: () => Int = () => {
      if (!done) {
        result = generator()
        done = true
      }
      result
    }
    Array(cancel, run, cancelled)
  }
}
