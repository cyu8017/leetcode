// LeetCode 2234 - Maximum Total Beauty of the Gardens
// https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/

object Solution {
  def maximumBeauty(flowers: Array[Int], newFlowers: Long, target: Int, full: Int, partial: Int): Long = {
    val n = flowers.length
    var i = 0
    while (i < n) {
      if (flowers(i) > target) flowers(i) = target
      i += 1
    }
    java.util.Arrays.sort(flowers)
    var sum = 0L
    for (f <- flowers) sum += f
    if (target.toLong * n - sum <= newFlowers) return n.toLong * full
    val pref = new Array[Long](n + 1)
    i = 0
    while (i < n) {
      pref(i + 1) = pref(i) + flowers(i)
      i += 1
    }
    var ans = 0L
    var j = n - 1
    var remain = newFlowers
    var complete = 0
    while (complete <= n) {
      if (complete > 0) {
        val need = target.toLong - flowers(n - complete)
        if (remain < need) return ans
        remain -= need
      }
      while (j >= n - complete || (j >= 0 && flowers(j).toLong * (j + 1) - pref(j + 1) > remain)) j -= 1
      var partialVal = 0L
      if (j >= 0) {
        val extra = (remain - (flowers(j).toLong * (j + 1) - pref(j + 1))) / (j + 1)
        partialVal = flowers(j) + extra
        if (partialVal >= target) partialVal = target - 1
      }
      ans = math.max(ans, complete.toLong * full + partialVal * partial)
      complete += 1
    }
    ans
  }
}
