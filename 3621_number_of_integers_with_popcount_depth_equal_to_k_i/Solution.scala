// LeetCode 3621 - Number of Integers With Popcount Depth Equal to K I
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/

object Solution {
  def popcountDepth(n: Long, k: Int): Long = {
    if (k == 0) return if (n >= 1) 1 else 0
    val sb = new StringBuilder
    var x = n
    while (x > 0) {
      sb.append(('0' + (x & 1).toInt).toChar)
      x >>= 1
    }
    var s = sb.reverse().toString
    if (s.isEmpty) s = "0"
    val memo = new java.util.HashMap[String, java.lang.Long]()

    def depth(x0: Int): Int = {
      if (x0 <= 0) return 100
      var x = x0
      var d = 0
      while (x > 1) {
        x = Integer.bitCount(x)
        d += 1
      }
      d
    }

    def dfs(pos: Int, tight: Int, started: Int, pc: Int): Long = {
      if (pos == s.length) {
        if (started == 0) return 0
        if (pc == 1) return if (k == 1) 1 else 0
        return if (depth(pc) == k - 1) 1 else 0
      }
      val key = pos + "," + tight + "," + started + "," + pc
      if (memo.containsKey(key)) return memo.get(key)
      val up = if (tight == 1) s.charAt(pos) - '0' else 1
      var res = 0L
      var dig = 0
      while (dig <= up) {
        val nt = if (tight == 1 && dig == up) 1 else 0
        if (started == 0 && dig == 0) res += dfs(pos + 1, nt, 0, 0)
        else res += dfs(pos + 1, nt, 1, pc + dig)
        dig += 1
      }
      memo.put(key, res)
      res
    }

    dfs(0, 1, 0, 0)
  }
}
