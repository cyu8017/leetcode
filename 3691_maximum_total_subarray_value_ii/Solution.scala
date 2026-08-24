// LeetCode 3691 - Maximum Total Subarray Value II
// https://leetcode.com/problems/maximum-total-subarray-value-ii/

object Solution {
  private class SparseTableRMQ(data: Array[Int]) {
    val n = data.length
    var maxLog = 0
    while ((1 << maxLog) <= n) maxLog += 1
    maxLog += 1
    val fMax = Array.ofDim[Int](n, maxLog)
    val fMin = Array.ofDim[Int](n, maxLog)
    val lg = new Array[Int](n + 1)
    var i = 2
    while (i <= n) {
      lg(i) = lg(i >> 1) + 1
      i += 1
    }
    i = 0
    while (i < n) {
      fMax(i)(0) = data(i)
      fMin(i)(0) = data(i)
      i += 1
    }
    var j = 1
    while (j < maxLog) {
      i = 0
      while (i <= n - (1 << j)) {
        fMax(i)(j) = math.max(fMax(i)(j - 1), fMax(i + (1 << (j - 1)))(j - 1))
        fMin(i)(j) = math.min(fMin(i)(j - 1), fMin(i + (1 << (j - 1)))(j - 1))
        i += 1
      }
      j += 1
    }

    def queryMax(l: Int, r: Int): Int = {
      val k = lg(r - l + 1)
      math.max(fMax(l)(k), fMax(r - (1 << k) + 1)(k))
    }

    def queryMin(l: Int, r: Int): Int = {
      val k = lg(r - l + 1)
      math.min(fMin(l)(k), fMin(r - (1 << k) + 1)(k))
    }
  }

  def maxTotalValue(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    val st = new SparseTableRMQ(nums)
    val pq = new java.util.PriorityQueue[Array[Long]]((a: Array[Long], b: Array[Long]) => java.lang.Long.compare(b(0), a(0)))
    var l = 0
    while (l < n) {
      val `val` = st.queryMax(l, n - 1).toLong - st.queryMin(l, n - 1)
      pq.offer(Array(`val`, l.toLong, (n - 1).toLong))
      l += 1
    }
    var ans = 0L
    var i = 0
    while (i < k) {
      val top = pq.poll()
      val v = top(0)
      val ll = top(1).toInt
      val r = top(2).toInt
      ans += v
      if (r > ll) {
        val nextVal = st.queryMax(ll, r - 1).toLong - st.queryMin(ll, r - 1)
        pq.offer(Array(nextVal, ll.toLong, (r - 1).toLong))
      }
      i += 1
    }
    ans
  }
}
