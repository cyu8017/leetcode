// LeetCode 2382 - Maximum Segment Sum After Removals
// https://leetcode.com/problems/maximum-segment-sum-after-removals/

object Solution {
  def maximumSegmentSum(nums: Array[Int], removeQueries: Array[Int]): Array[Long] = {
    val n = nums.length
    val parent = Array.tabulate(n)(identity)
    val sum = Array.fill(n)(0L)
    val active = Array.fill(n)(false)

    def find(x0: Int): Int = {
      var x = x0
      while (parent(x) != x) {
        parent(x) = parent(parent(x))
        x = parent(x)
      }
      x
    }

    def unite(a: Int, b: Int): Unit = {
      val ra = find(a)
      val rb = find(b)
      if (ra == rb) return
      parent(rb) = ra
      sum(ra) += sum(rb)
    }

    val ans = Array.fill(n)(0L)
    var best = 0L
    var i = n - 1
    while (i >= 0) {
      ans(i) = best
      val idx = removeQueries(i)
      active(idx) = true
      sum(idx) = nums(idx)
      if (idx > 0 && active(idx - 1)) unite(idx, idx - 1)
      if (idx + 1 < n && active(idx + 1)) unite(idx, idx + 1)
      best = math.max(best, sum(find(idx)))
      i -= 1
    }
    ans
  }
}
