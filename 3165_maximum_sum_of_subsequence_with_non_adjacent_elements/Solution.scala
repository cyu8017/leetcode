// LeetCode 3165 - Maximum Sum of Subsequence With Non-adjacent Elements
// https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/

object Solution {
  private class Node {
    var l = 0
    var r = 0
    var s00 = 0
    var s01 = 0
    var s10 = 0
    var s11 = 0
  }

  def maximumSumSubsequence(nums: Array[Int], queries: Array[Array[Int]]): Int = {
    val n = nums.length
    val tr = Array.fill(n * 4)(new Node())

    def build(u: Int, l: Int, r: Int): Unit = {
      tr(u).l = l
      tr(u).r = r
      if (l == r) return
      val mid = (l + r) >> 1
      build(u << 1, l, mid)
      build(u << 1 | 1, mid + 1, r)
    }

    def pushup(u: Int): Unit = {
      val left = tr(u << 1)
      val right = tr(u << 1 | 1)
      tr(u).s00 = math.max(left.s00 + right.s10, left.s01 + right.s00)
      tr(u).s01 = math.max(left.s00 + right.s11, left.s01 + right.s01)
      tr(u).s10 = math.max(left.s10 + right.s10, left.s11 + right.s00)
      tr(u).s11 = math.max(left.s10 + right.s11, left.s11 + right.s01)
    }

    def modify(u: Int, x: Int, v: Int): Unit = {
      if (tr(u).l == tr(u).r) {
        tr(u).s11 = math.max(0, v)
        return
      }
      val mid = (tr(u).l + tr(u).r) >> 1
      if (x <= mid) modify(u << 1, x, v)
      else modify(u << 1 | 1, x, v)
      pushup(u)
    }

    def query(u: Int, l: Int, r: Int): Int = {
      if (tr(u).l >= l && tr(u).r <= r) return tr(u).s11
      val mid = (tr(u).l + tr(u).r) >> 1
      var ans = 0
      if (r <= mid) ans = query(u << 1, l, r)
      if (l > mid) ans = math.max(ans, query(u << 1 | 1, l, r))
      ans
    }

    build(1, 1, n)
    var i = 0
    while (i < n) {
      modify(1, i + 1, nums(i))
      i += 1
    }
    val MOD = 1000000007
    var ans = 0
    queries.foreach { q =>
      modify(1, q(0) + 1, q(1))
      ans = (ans + query(1, 1, n)) % MOD
    }
    ans
  }
}
