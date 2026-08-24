// LeetCode 2676 - Throttle
// https://leetcode.com/problems/throttle/

object Solution {
  def throttle(fn: () => Unit, t: Int): () => Unit = {
    var last = System.nanoTime() - 24L * 3600 * 1000000000L
    () => {
      val now = System.nanoTime()
      if ((now - last) / 1000000L >= t) {
        last = now
        fn()
      }
    }
  }
}
