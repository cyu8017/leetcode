// LeetCode 2172 - Maximum AND Sum of Array
// https://leetcode.com/problems/maximum-and-sum-of-array/

object Solution {
  def maximumANDSum(nums: Array[Int], numSlots: Int): Int = {
    val n = nums.length
    val slots = numSlots
    var maxMask = 1
    var i = 0
    while (i < slots) { maxMask *= 3; i += 1 }
    val dp = Array.fill(maxMask)(0)
    var mask = 0
    while (mask < maxMask) {
      var cnt = 0
      var x = mask
      while (x > 0) { cnt += x % 3; x /= 3 }
      if (cnt < n) {
        val v = nums(cnt)
        var bas = 1
        var s = 1
        while (s <= slots) {
          val occ = (mask / bas) % 3
          if (occ < 2) {
            val nm = mask + bas
            dp(nm) = math.max(dp(nm), dp(mask) + (v & s))
          }
          bas *= 3
          s += 1
        }
      }
      mask += 1
    }
    var best = 0
    dp.foreach(v => best = math.max(best, v))
    best
  }
}
