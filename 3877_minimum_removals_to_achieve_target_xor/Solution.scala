// LeetCode 3877 - Minimum Removals To Achieve Target Xor
// https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/

object Solution {
  def minRemovals(nums: Array[Int], target: Int): Int = {
    var mx = 0
    nums.foreach { x => mx = math.max(mx, x) }
    var m = 0
    if (mx > 0) {
      var u = mx
      while (u != 0) { m += 1; u >>= 1 }
    }
    if ((1 << m) <= target) return -1
    val n = nums.length
    val N = 1 << m
    val f = Array.ofDim[Int](n + 1, N)
    var i = 0
    while (i <= n) {
      java.util.Arrays.fill(f(i), Int.MinValue)
      i += 1
    }
    f(0)(0) = 0
    i = 1
    while (i <= n) {
      val x = nums(i - 1)
      var j = 0
      while (j < N) {
        f(i)(j) = f(i - 1)(j)
        if (f(i - 1)(j ^ x) != Int.MinValue) {
          f(i)(j) = math.max(f(i)(j), f(i - 1)(j ^ x) + 1)
        }
        j += 1
      }
      i += 1
    }
    if (f(n)(target) < 0) return -1
    n - f(n)(target)
  }
}
