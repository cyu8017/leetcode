// LeetCode 3628 - Maximum Number of Subsequences After One Inserting
// https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/

object Solution {
  private def calc(s: String, t: String): Long = {
    var cnt = 0L
    var a = 0L
    s.foreach { c =>
      if (c == t.charAt(1)) cnt += a
      if (c == t.charAt(0)) a += 1
    }
    cnt
  }

  def numOfSubsequences(s: String): Long = {
    var l = 0L
    var r = 0L
    s.foreach { c => if (c == 'T') r += 1 }
    var ans = 0L
    var mx = 0L
    s.foreach { c =>
      if (c == 'T') r -= 1
      if (c == 'C') ans += l * r
      if (c == 'L') l += 1
      mx = math.max(mx, l * r)
    }
    mx = math.max(mx, math.max(calc(s, "LC"), calc(s, "CT")))
    ans + mx
  }
}
