// LeetCode 1756 - Design Most Recently Used Queue
// https://leetcode.com/problems/design-most-recently-used-queue/

class MRUQueue(_n: Int) {
  private val q = scala.collection.mutable.ArrayBuffer.range(1, _n + 1)

  def fetch(k: Int): Int = {
    val value = q.remove(k - 1)
    q.append(value)
    value
  }
}
