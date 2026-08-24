// LeetCode 3630 - Partition Array for Maximum XOR and AND
// https://leetcode.com/problems/partition-array-for-maximum-xor-and-and/

object Solution {
  def maximizeXorAndXor(nums: Array[Int]): Long = {
    val n = nums.length
    var best = 0L
    var mask = 0
    while (mask < (1 << n)) {
      var andVal = -1
      var xorRest = 0
      var i = 0
      while (i < n) {
        if (((mask >> i) & 1) != 0) {
          andVal = if (andVal < 0) nums(i) else (andVal & nums(i))
        } else {
          xorRest ^= nums(i)
        }
        i += 1
      }
      if (andVal < 0) andVal = 0
      val comp = ((1 << n) - 1) ^ mask
      var sub = comp
      var done = false
      while (!done) {
        var x1 = 0
        i = 0
        while (i < n) {
          if (((sub >> i) & 1) != 0) x1 ^= nums(i)
          i += 1
        }
        val x2 = xorRest ^ x1
        best = math.max(best, andVal.toLong + x1 + x2)
        if (sub == 0) done = true
        else sub = (sub - 1) & comp
      }
      mask += 1
    }
    best
  }
}
