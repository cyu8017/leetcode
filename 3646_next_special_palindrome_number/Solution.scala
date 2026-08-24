// LeetCode 3646 - Next Special Palindrome Number
// https://leetcode.com/problems/next-special-palindrome-number/

object Solution {
  def specialPalindrome(n: Long): Long = {
    val cands = new java.util.ArrayList[java.lang.Long]()
    var halfCnt = new Array[Int](10)
    var mid = 0
    var halfLen = 0

    def dfs(pos: Int, cur: java.util.List[Integer]): Unit = {
      if (pos == halfLen) {
        val left = new StringBuilder
        val it = cur.iterator()
        while (it.hasNext) left.append(it.next().intValue())
        val s = new StringBuilder(left)
        if (mid > 0) s.append(mid)
        var i = left.length - 1
        while (i >= 0) {
          s.append(left.charAt(i))
          i -= 1
        }
        cands.add(java.lang.Long.parseLong(s.toString))
        return
      }
      var d = 1
      while (d <= 9) {
        if (halfCnt(d) != 0) {
          halfCnt(d) -= 1
          cur.add(d)
          dfs(pos + 1, cur)
          cur.remove(cur.size() - 1)
          halfCnt(d) += 1
        }
        d += 1
      }
    }

    def gen(mask: Int): Unit = {
      var total = 0
      var odd = 0
      var d = 1
      while (d <= 9) {
        if (((mask >> d) & 1) != 0) {
          total += d
          if (d % 2 == 1) odd += 1
        }
        d += 1
      }
      if (total == 0 || total > 18 || odd > 1) return
      halfCnt = new Array[Int](10)
      mid = 0
      d = 1
      while (d <= 9) {
        if (((mask >> d) & 1) != 0) {
          halfCnt(d) = d / 2
          if (d % 2 == 1) mid = d
        }
        d += 1
      }
      halfLen = total / 2
      dfs(0, new java.util.ArrayList[Integer]())
    }

    var mask = 1
    while (mask < (1 << 10)) {
      if ((mask & 1) == 0) gen(mask)
      mask += 1
    }
    java.util.Collections.sort(cands)
    val it = cands.iterator()
    while (it.hasNext) {
      val v = it.next().longValue()
      if (v > n) return v
    }
    -1L
  }
}
