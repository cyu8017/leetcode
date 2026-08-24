// LeetCode 3934 - Smallest Unique Subarray
// https://leetcode.com/problems/smallest-unique-subarray/

object Solution {
  def smallestUniqueSubarray(nums: Array[Int]): Int = {
    val n = nums.length
    val sa = Array.tabulate(n)(i => i)
    var rank = nums.clone()
    var width = 1
    while (width < n) {
      val w = width
      val r = rank
      val sorted = sa.sortWith { (ia, ib) =>
        if (r(ia) != r(ib)) r(ia) < r(ib)
        else {
          val ra = if (ia + w < n) r(ia + w) else -1
          val rb = if (ib + w < n) r(ib + w) else -1
          ra < rb
        }
      }
      var i = 0
      while (i < n) {
        sa(i) = sorted(i)
        i += 1
      }
      val next = new Array[Int](n)
      i = 1
      while (i < n) {
        val a = sa(i - 1)
        val b = sa(i)
        val different = rank(a) != rank(b)
        val ra = if (a + width < n) rank(a + width) else -1
        val rb = if (b + width < n) rank(b + width) else -1
        next(b) = if (different || ra != rb) next(a) + 1 else next(a)
        i += 1
      }
      rank = next
      if (rank(sa(n - 1)) == n - 1) width = n
      else width <<= 1
    }
    val pos = new Array[Int](n)
    var i = 0
    while (i < n) {
      pos(sa(i)) = i
      i += 1
    }
    val lcp = new Array[Int](math.max(0, n - 1))
    var height = 0
    i = 0
    while (i < n) {
      val p = pos(i)
      if (p == n - 1) height = 0
      else {
        val j = sa(p + 1)
        while (i + height < n && j + height < n && nums(i + height) == nums(j + height)) height += 1
        lcp(p) = height
        if (height > 0) height -= 1
      }
      i += 1
    }
    var ans = n
    var p = 0
    while (p < n) {
      val start = sa(p)
      var need = 1
      if (p > 0 && lcp(p - 1) + 1 > need) need = lcp(p - 1) + 1
      if (p + 1 < n && lcp(p) + 1 > need) need = lcp(p) + 1
      if (need <= n - start && need < ans) ans = need
      p += 1
    }
    ans
  }
}
