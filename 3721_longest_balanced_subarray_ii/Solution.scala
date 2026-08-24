// LeetCode 3721 - Longest Balanced Subarray II
// https://leetcode.com/problems/longest-balanced-subarray-ii/

object Solution {
  private class Node {
    var l: Int = 0
    var r: Int = 0
    var mn: Int = 0
    var mx: Int = 0
    var lz: Int = 0
  }

  private class SegmentTree(n: Int) {
    val tr: Array[Node] = Array.fill(n << 2)(new Node())
    build(1, 0, n)

    def build(u: Int, l: Int, r: Int): Unit = {
      tr(u).l = l; tr(u).r = r; tr(u).mn = 0; tr(u).mx = 0; tr(u).lz = 0
      if (l == r) return
      val mid = (l + r) >> 1
      build(u << 1, l, mid)
      build(u << 1 | 1, mid + 1, r)
    }

    def apply(u: Int, v: Int): Unit = {
      tr(u).mn += v
      tr(u).mx += v
      tr(u).lz += v
    }

    def pushup(u: Int): Unit = {
      tr(u).mn = math.min(tr(u << 1).mn, tr(u << 1 | 1).mn)
      tr(u).mx = math.max(tr(u << 1).mx, tr(u << 1 | 1).mx)
    }

    def pushdown(u: Int): Unit = {
      if (tr(u).lz != 0) {
        val v = tr(u).lz
        apply(u << 1, v)
        apply(u << 1 | 1, v)
        tr(u).lz = 0
      }
    }

    def modify(u: Int, l: Int, r: Int, v: Int): Unit = {
      if (tr(u).l >= l && tr(u).r <= r) {
        apply(u, v)
        return
      }
      pushdown(u)
      val mid = (tr(u).l + tr(u).r) >> 1
      if (l <= mid) modify(u << 1, l, r, v)
      if (r > mid) modify(u << 1 | 1, l, r, v)
      pushup(u)
    }

    def query(u: Int, target: Int): Int = {
      if (tr(u).l == tr(u).r) return tr(u).l
      pushdown(u)
      val left = u << 1
      val right = u << 1 | 1
      if (tr(left).mn <= target && target <= tr(left).mx) query(left, target)
      else query(right, target)
    }
  }

  def longestBalanced(nums: Array[Int]): Int = {
    val n = nums.length
    val st = new SegmentTree(n)
    val last = new java.util.HashMap[Integer, Integer]()
    var now = 0
    var ans = 0
    var i = 1
    while (i <= n) {
      val x = nums(i - 1)
      val det = if ((x & 1) != 0) 1 else -1
      if (last.containsKey(x)) {
        st.modify(1, last.get(x), n, -det)
        now -= det
      }
      last.put(x, i)
      st.modify(1, i, n, det)
      now += det
      val pos = st.query(1, now)
      ans = math.max(ans, i - pos)
      i += 1
    }
    ans
  }
}
