// LeetCode 2612 - Minimum Reverse Operations
// https://leetcode.com/problems/minimum-reverse-operations/

object Solution {
  def minReverseOperations(n: Int, p: Int, banned: Array[Int], k: Int): Array[Int] = {
    val ban = banned.toSet
    val ans = Array.fill(n)(-1)
    ans(p) = 0
    val q = scala.collection.mutable.Queue[Array[Int]]()
    q.enqueue(Array(p, 0))
    while (q.nonEmpty) {
      val cur = q.dequeue()
      val i = cur(0)
      val d = cur(1)
      var lo = i - (k - 1)
      if (lo < 0) lo = 0
      var hi = i
      if (hi > n - k) hi = n - k
      var L = lo
      while (L <= hi) {
        val R = L + k - 1
        val ni = L + R - i
        if (ni >= 0 && ni < n && !ban.contains(ni) && ans(ni) == -1) {
          ans(ni) = d + 1
          q.enqueue(Array(ni, d + 1))
        }
        L += 1
      }
    }
    ans
  }
}
