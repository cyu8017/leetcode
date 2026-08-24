// LeetCode 2569 - Handling Sum Queries After Update
// https://leetcode.com/problems/handling-sum-queries-after-update/

object Solution {
  def handleQuery(nums1: Array[Int], nums2: Array[Int], queries: Array[Array[Int]]): Array[Long] = {
    val n = nums1.length
    val ones = Array.fill(4 * n)(0)
    val lazy = Array.fill(4 * n)(false)

    def build(idx: Int, l: Int, r: Int): Unit = {
      if (l == r) {
        ones(idx) = nums1(l)
        return
      }
      val m = (l + r) / 2
      build(idx * 2, l, m)
      build(idx * 2 + 1, m + 1, r)
      ones(idx) = ones(idx * 2) + ones(idx * 2 + 1)
    }

    def apply(idx: Int, l: Int, r: Int): Unit = {
      ones(idx) = (r - l + 1) - ones(idx)
      lazy(idx) = !lazy(idx)
    }

    def push(idx: Int, l: Int, r: Int): Unit = {
      if (lazy(idx) && l != r) {
        val m = (l + r) / 2
        apply(idx * 2, l, m)
        apply(idx * 2 + 1, m + 1, r)
        lazy(idx) = false
      }
    }

    def update(idx: Int, l: Int, r: Int, ql: Int, qr: Int): Unit = {
      if (ql <= l && r <= qr) {
        apply(idx, l, r)
        return
      }
      push(idx, l, r)
      val m = (l + r) / 2
      if (ql <= m) update(idx * 2, l, m, ql, qr)
      if (qr > m) update(idx * 2 + 1, m + 1, r, ql, qr)
      ones(idx) = ones(idx * 2) + ones(idx * 2 + 1)
    }

    build(1, 0, n - 1)
    var sum2 = 0L
    nums2.foreach(x => sum2 += x)
    val ans = scala.collection.mutable.ArrayBuffer.empty[Long]
    queries.foreach { q =>
      if (q(0) == 1) update(1, 0, n - 1, q(1), q(2))
      else if (q(0) == 2) sum2 += q(1).toLong * ones(1)
      else ans += sum2
    }
    ans.toArray
  }
}
