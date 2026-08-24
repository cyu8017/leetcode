// LeetCode 2983 - Palindrome Rearrangement Queries
// https://leetcode.com/problems/palindrome-rearrangement-queries/

object Solution {
  def canMakePalindromeQueries(s0: String, queries: Array[Array[Int]]): Array[Boolean] = {
    val n = s0.length
    val m = n / 2
    val tArr = s0.substring(m).toCharArray
    var ii = 0
    var jj = tArr.length - 1
    while (ii < jj) { val tmp = tArr(ii); tArr(ii) = tArr(jj); tArr(jj) = tmp; ii += 1; jj -= 1 }
    val t = new String(tArr)
    val s = s0.substring(0, m)
    val pre1 = Array.ofDim[Array[Int]](m + 1)
    val pre2 = Array.ofDim[Array[Int]](m + 1)
    val diff = Array.ofDim[Int](m + 1)
    pre1(0) = Array.ofDim[Int](26)
    pre2(0) = Array.ofDim[Int](26)
    var i = 1
    while (i <= m) {
      pre1(i) = pre1(i - 1).clone()
      pre2(i) = pre2(i - 1).clone()
      pre1(i)(s.charAt(i - 1) - 'a') += 1
      pre2(i)(t.charAt(i - 1) - 'a') += 1
      diff(i) = diff(i - 1) + (if (s.charAt(i - 1) == t.charAt(i - 1)) 0 else 1)
      i += 1
    }

    def count(pre: Array[Array[Int]], a: Int, b: Int): Array[Int] = {
      val cnt = Array.ofDim[Int](26)
      var k = 0
      while (k < 26) { cnt(k) = pre(b + 1)(k) - pre(a)(k); k += 1 }
      cnt
    }
    def sub(cnt1: Array[Int], cnt2: Array[Int]): Array[Int] = {
      val cnt = Array.ofDim[Int](26)
      var i = 0
      while (i < 26) {
        cnt(i) = cnt1(i) - cnt2(i)
        if (cnt(i) < 0) return null
        i += 1
      }
      cnt
    }
    def eq(a: Array[Int], b: Array[Int]): Boolean = {
      var i = 0
      while (i < 26) { if (a(i) != b(i)) return false; i += 1 }
      true
    }
    def check(p1: Array[Array[Int]], p2: Array[Array[Int]], a: Int, b: Int, c: Int, d: Int): Boolean = {
      if (diff(a) > 0 || diff(diff.length - 1) - diff(math.max(b, d) + 1) > 0) return false
      if (d <= b) return eq(count(p1, a, b), count(p2, a, b))
      if (b < c) {
        return diff(c) - diff(b + 1) == 0 && eq(count(p1, a, b), count(p2, a, b)) &&
          eq(count(p1, c, d), count(p2, c, d))
      }
      val cnt1 = sub(count(p1, a, b), count(p2, a, c - 1))
      val cnt2 = sub(count(p2, c, d), count(p1, b + 1, d))
      cnt1 != null && cnt2 != null && eq(cnt1, cnt2)
    }

    val ans = Array.ofDim[Boolean](queries.length)
    i = 0
    while (i < queries.length) {
      val q = queries(i)
      val a = q(0)
      val b = q(1)
      val c = n - 1 - q(3)
      val d = n - 1 - q(2)
      ans(i) = if (a <= c) check(pre1, pre2, a, b, c, d) else check(pre2, pre1, c, d, a, b)
      i += 1
    }
    ans
  }
}
