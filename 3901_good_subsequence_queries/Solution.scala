// LeetCode 3901 - Good Subsequence Queries
// https://leetcode.com/problems/good-subsequence-queries/

object Solution {
  private class Node {
    var l = 0
    var r = 0
    var g = 0
  }

  private class SegmentTree(n: Int) {
    val tr: Array[Node] = Array.fill(n << 2)(new Node)
    build(1, 1, n)

    def build(u: Int, l: Int, r: Int): Unit = {
      tr(u).l = l
      tr(u).r = r
      tr(u).g = 0
      if (l == r) return
      val mid = (l + r) >> 1
      build(u << 1, l, mid)
      build(u << 1 | 1, mid + 1, r)
    }

    def pushup(u: Int): Unit = { tr(u).g = gcd(tr(u << 1).g, tr(u << 1 | 1).g) }

    def modify(u: Int, x: Int, v: Int): Unit = {
      if (tr(u).l == tr(u).r) { tr(u).g = v; return }
      val mid = (tr(u).l + tr(u).r) >> 1
      if (x <= mid) modify(u << 1, x, v)
      else modify(u << 1 | 1, x, v)
      pushup(u)
    }

    def query(u: Int, l: Int, r: Int): Int = {
      if (l > r) return 0
      if (tr(u).l >= l && tr(u).r <= r) return tr(u).g
      val mid = (tr(u).l + tr(u).r) >> 1
      if (r <= mid) return query(u << 1, l, r)
      if (l > mid) return query(u << 1 | 1, l, r)
      gcd(query(u << 1, l, mid), query(u << 1 | 1, mid + 1, r))
    }
  }

  private def gcd(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }

  def countGoodSubseq(nums: Array[Int], p: Int, queries: Array[Array[Int]]): Int = {
    val n = nums.length
    val tree = new SegmentTree(n)
    var cnt = 0
    var i = 0
    while (i < n) {
      if (nums(i) % p == 0) {
        tree.modify(1, i + 1, nums(i))
        cnt += 1
      }
      i += 1
    }
    var ans = 0
    queries.foreach { q =>
      val idx = q(0)
      val value = q(1)
      if (nums(idx) % p == 0) {
        tree.modify(1, idx + 1, 0)
        cnt -= 1
      }
      if (value % p == 0) {
        tree.modify(1, idx + 1, value)
        cnt += 1
      }
      nums(idx) = value
      if (tree.tr(1).g == p) {
        if (cnt < n || n > 6) ans += 1
        else {
          var found = false
          i = 1
          while (i <= n && !found) {
            val leftG = tree.query(1, 1, i - 1)
            val rightG = tree.query(1, i + 1, n)
            if (gcd(leftG, rightG) == p) { ans += 1; found = true }
            i += 1
          }
        }
      }
    }
    ans
  }
}
