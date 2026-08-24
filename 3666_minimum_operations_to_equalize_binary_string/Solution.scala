// LeetCode 3666 - Minimum Operations to Equalize Binary String
// https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/

object Solution {
  def minOperations(s: String, k: Int): Int = {
    val n = s.length
    val ts = Array.fill(2)(new java.util.TreeSet[Integer]())
    var i = 0
    while (i <= n) {
      ts(i % 2).add(i)
      i += 1
    }
    var cnt0 = 0
    for (c <- s) if (c == '0') cnt0 += 1
    ts(cnt0 % 2).remove(cnt0)
    var q = new java.util.ArrayList[Integer]()
    q.add(cnt0)
    var ans = 0
    while (!q.isEmpty) {
      val nq = new java.util.ArrayList[Integer]()
      val qit = q.iterator()
      while (qit.hasNext) {
        val cur = qit.next().intValue()
        if (cur == 0) return ans
        val l = cur + k - 2 * math.min(cur, k)
        val r = cur + k - 2 * math.max(k - n + cur, 0)
        val t = ts(l % 2)
        var it = t.ceiling(l)
        while (it != null && it <= r) {
          nq.add(it)
          t.remove(it)
          it = t.ceiling(l)
        }
      }
      q = nq
      ans += 1
    }
    -1
  }
}
