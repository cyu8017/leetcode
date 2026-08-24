// LeetCode 3670 - Maximum Product of Two Integers With No Common Bits
// https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/

object Solution {
  def maxProduct(nums: Array[Int]): Long = {
    var maxV = 0
    for (v <- nums) if (v > maxV) maxV = v
    var bitsN = 0
    var x = maxV
    while (x > 0) {
      bitsN += 1
      x >>= 1
    }
    if (bitsN == 0) bitsN = 1
    val size = 1 << bitsN
    val best = new Array[Int](size)
    for (v <- nums) if (v > best(v)) best(v) = v
    var mask = 0
    while (mask < size) {
      var b = 0
      while (b < bitsN) {
        if ((mask & (1 << b)) != 0) {
          val sub = mask ^ (1 << b)
          if (best(sub) > best(mask)) best(mask) = best(sub)
        }
        b += 1
      }
      mask += 1
    }
    var ans = 0L
    for (v <- nums) {
      val comp = (size - 1) ^ v
      if (best(comp) > 0) {
        val p = v.toLong * best(comp)
        if (p > ans) ans = p
      }
    }
    ans
  }
}
