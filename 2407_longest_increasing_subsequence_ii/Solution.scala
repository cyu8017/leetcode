// LeetCode 2407 - Longest Increasing Subsequence II
// https://leetcode.com/problems/longest-increasing-subsequence-ii/

object Solution {
  def lengthOfLIS(nums: Array[Int], k: Int): Int = {
    var maxV = 0
    nums.foreach(x => maxV = math.max(maxV, x))
    val st = new SegTree(maxV + 1)
    var ans = 0
    nums.foreach { x =>
      val lo = math.max(1, x - k)
      var best = 1
      if (lo <= x - 1) best = st.query(1, 1, maxV, lo, x - 1) + 1
      st.update(1, 1, maxV, x, best)
      ans = math.max(ans, best)
    }
    ans
  }

  private class SegTree(n: Int) {
    private val tree = Array.fill(4 * n)(0)

    def update(idx: Int, l: Int, r: Int, pos: Int, value: Int): Unit = {
      if (l == r) {
        tree(idx) = math.max(tree(idx), value)
        return
      }
      val mid = (l + r) / 2
      if (pos <= mid) update(idx * 2, l, mid, pos, value)
      else update(idx * 2 + 1, mid + 1, r, pos, value)
      tree(idx) = math.max(tree(idx * 2), tree(idx * 2 + 1))
    }

    def query(idx: Int, l: Int, r: Int, ql: Int, qr: Int): Int = {
      if (qr < l || r < ql) return 0
      if (ql <= l && r <= qr) return tree(idx)
      val mid = (l + r) / 2
      math.max(query(idx * 2, l, mid, ql, qr), query(idx * 2 + 1, mid + 1, r, ql, qr))
    }
  }
}
