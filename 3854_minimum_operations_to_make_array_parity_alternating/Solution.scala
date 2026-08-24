// LeetCode 3854 - Minimum Operations To Make Array Parity Alternating
// https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/

object Solution {
  def makeParityAlternating(nums: Array[Int]): Array[Int] = {
    if (nums.length == 1) return Array(0, 0)
    var mn = nums(0)
    var mx = nums(0)
    nums.foreach { x =>
      mn = math.min(mn, x)
      mx = math.max(mx, x)
    }
    val r0 = f(nums, 0, mn, mx)
    val r1 = f(nums, 1, mn, mx)
    if (r0(0) != r1(0)) {
      if (r0(0) < r1(0)) r0 else r1
    } else if (r0(1) <= r1(1)) r0
    else r1
  }

  private def f(nums: Array[Int], k: Int, mn: Int, mx: Int): Array[Int] = {
    var cnt = 0
    var a = Int.MaxValue
    var b = Int.MinValue
    var i = 0
    while (i < nums.length) {
      var x = nums(i)
      if (((x - i) & 1) != k) {
        cnt += 1
        if (x == mn) x += 1
        else if (x == mx) x -= 1
      }
      a = math.min(a, x)
      b = math.max(b, x)
      i += 1
    }
    Array(cnt, math.max(1, b - a))
  }
}
