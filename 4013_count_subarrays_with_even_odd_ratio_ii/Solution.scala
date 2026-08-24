// LeetCode 4013 - Count Subarrays With Even Odd Ratio II
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/

object Solution {
  def countRatioSubarrays(nums: Array[Int], a: Int, b: Int): Long = {
    val n = nums.length
    val s = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      if (nums(i) % 2 == 1) s(i + 1) = s(i) + a
      else s(i + 1) = s(i) - b
      i += 1
    }
    var st = s.clone()
    java.util.Arrays.sort(st)
    var uniq = 0
    i = 0
    while (i < st.length) {
      if (uniq == 0 || st(i) != st(uniq - 1)) {
        st(uniq) = st(i)
        uniq += 1
      }
      i += 1
    }
    st = st.take(uniq)
    val bit = new BIT(st.length + 1)
    var ans = 0L
    for (v <- s) {
      val x = lowerBound(st, v) + 1
      ans += bit.query(x)
      bit.update(x, 1)
    }
    ans
  }

  private def lowerBound(a: Array[Long], x: Long): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) >>> 1
      if (a(mid) < x) lo = mid + 1
      else hi = mid
    }
    lo
  }

  private class BIT(n: Int) {
    private val c = new Array[Int](n + 1)

    def update(x0: Int, delta: Int): Unit = {
      var x = x0
      while (x <= n) {
        c(x) += delta
        x += x & -x
      }
    }

    def query(x0: Int): Int = {
      var sum = 0
      var x = x0
      while (x > 0) {
        sum += c(x)
        x -= x & -x
      }
      sum
    }
  }
}
