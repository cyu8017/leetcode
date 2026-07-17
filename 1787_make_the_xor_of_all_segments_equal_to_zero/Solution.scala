// LeetCode 1787 - Make the XOR of All Segments Equal to Zero
// https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/

object Solution {
  def minChanges(nums: Array[Int], k: Int): Int = {
    val freq = Array.ofDim[Int](k, 1024)
    val size = new Array[Int](k)
    for (i <- nums.indices) {
      freq(i % k)(nums(i)) += 1
      size(i % k) += 1
    }
    val inf = 1000000000
    var dp = Array.fill(256)(inf)
    dp(0) = 0
    for (i <- 0 until k) {
      val ndp = Array.fill(256)(inf)
      for (xv <- 0 until 256) {
        val cost = size(i) - freq(i)(xv)
        for (xo <- 0 until 256) {
          if (dp(xo) != inf) {
            val key = xo ^ xv
            if (dp(xo) + cost < ndp(key)) {
              ndp(key) = dp(xo) + cost
            }
          }
        }
      }
      dp = ndp
    }
    dp(0)
  }
}
