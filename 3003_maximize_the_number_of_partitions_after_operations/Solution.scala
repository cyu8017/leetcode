// LeetCode 3003 - Maximize the Number of Partitions After Operations
// https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/

object Solution {
  private def popcount(x0: Int): Int = {
    var x = x0
    var c = 0
    while (x != 0) { c += x & 1; x >>= 1 }
    c
  }

  def maxPartitionsAfterOperations(s: String, k: Int): Int = {
    val n = s.length
    val memo = scala.collection.mutable.HashMap[Long, Int]()
    def key(i: Int, cur: Int, t: Int): Long = (i.toLong << 32) | (cur.toLong << 1) | t
    def dfs(i: Int, cur: Int, t: Int): Int = {
      if (i >= n) return 1
      val kkey = key(i, cur, t)
      if (memo.contains(kkey)) return memo(kkey)
      val v = 1 << (s.charAt(i) - 'a')
      var nxt = cur | v
      var ans = if (popcount(nxt) > k) dfs(i + 1, v, t) + 1 else dfs(i + 1, nxt, t)
      if (t > 0) {
        var j = 0
        while (j < 26) {
          nxt = cur | (1 << j)
          if (popcount(nxt) > k) ans = math.max(ans, dfs(i + 1, 1 << j, 0) + 1)
          else ans = math.max(ans, dfs(i + 1, nxt, 0))
          j += 1
        }
      }
      memo(kkey) = ans
      ans
    }
    dfs(0, 0, 1)
  }
}
