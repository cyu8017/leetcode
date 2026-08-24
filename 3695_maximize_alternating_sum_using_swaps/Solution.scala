// LeetCode 3695 - Maximize Alternating Sum Using Swaps
// https://leetcode.com/problems/maximize-alternating-sum-using-swaps/

object Solution {
  def maxAlternatingSum(nums: Array[Int], swaps: Array[Array[Int]]): Long = {
    val n = nums.length
    val parent = Array.tabulate(n)(i => i)

    def find(x: Int): Int = {
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }

    for (s <- swaps) {
      val a = find(s(0))
      val b = find(s(1))
      if (a != b) parent(a) = b
    }
    val compVals = new java.util.HashMap[Integer, java.util.List[Integer]]()
    val compIdx = new java.util.HashMap[Integer, java.util.List[Integer]]()
    var i = 0
    while (i < n) {
      val r = find(i)
      compVals.computeIfAbsent(r, _ => new java.util.ArrayList[Integer]()).add(nums(i))
      compIdx.computeIfAbsent(r, _ => new java.util.ArrayList[Integer]()).add(i)
      i += 1
    }
    val arr = new Array[Int](n)
    val it = compVals.entrySet().iterator()
    while (it.hasNext) {
      val e = it.next()
      val r = e.getKey
      val vals = e.getValue
      val idxs = compIdx.get(r)
      vals.sort(java.util.Collections.reverseOrder())
      val even = new java.util.ArrayList[Integer]()
      val odd = new java.util.ArrayList[Integer]()
      val iit = idxs.iterator()
      while (iit.hasNext) {
        val ii = iit.next().intValue()
        if (ii % 2 == 0) even.add(ii)
        else odd.add(ii)
      }
      java.util.Collections.sort(even)
      java.util.Collections.sort(odd)
      var ei = 0
      val vit = vals.iterator()
      while (vit.hasNext) {
        val v = vit.next().intValue()
        if (ei < even.size()) {
          arr(even.get(ei)) = v
          ei += 1
        } else {
          arr(odd.get(ei - even.size())) = v
          ei += 1
        }
      }
    }
    var ans = 0L
    i = 0
    while (i < n) {
      if (i % 2 == 0) ans += arr(i)
      else ans -= arr(i)
      i += 1
    }
    ans
  }
}
