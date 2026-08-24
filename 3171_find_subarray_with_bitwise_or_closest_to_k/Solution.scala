// LeetCode 3171 - Find Subarray With Bitwise OR Closest to K
// https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/

object Solution {
  def minimumDifference(nums: Array[Int], k: Int): Int = {
    var mx = 0
    for (v <- nums) mx = math.max(mx, v)
    val m = if (mx == 0) 1 else 32 - leadingZeroCount(mx)
    val cnt = Array.fill(m)(0)
    var ans = Int.MaxValue
    var s = 0
    var i = 0
    var j = 0
    while (j < nums.length) {
      val x = nums(j)
      s |= x
      ans = math.min(ans, math.abs(s - k))
      var h = 0
      while (h < m) {
        if (((x >> h) & 1) != 0) cnt(h) += 1
        h += 1
      }
      while (i < j && s > k) {
        val y = nums(i)
        h = 0
        while (h < m) {
          if (((y >> h) & 1) != 0) {
            cnt(h) -= 1
            if (cnt(h) == 0) s ^= 1 << h
          }
          h += 1
        }
        ans = math.min(ans, math.abs(s - k))
        i += 1
      }
      j += 1
    }
    ans
  }

  def leadingZeroCount(x: Int): Int = {
    if (x == 0) return 32
    var n = 0
    var bit = 31
    while (bit >= 0) {
      if (((x >> bit) & 1) != 0) return n
      n += 1
      bit -= 1
    }
    n
  }
}
