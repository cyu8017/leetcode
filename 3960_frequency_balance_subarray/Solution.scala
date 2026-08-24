// LeetCode 3960 - Frequency Balance Subarray
// https://leetcode.com/problems/frequency-balance-subarray/

import scala.collection.mutable

object Solution {
  def getLength(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 1
    var l = 0
    while (l < n) {
      val cnt = mutable.HashMap.empty[Int, Int]
      val freq = mutable.HashMap.empty[Int, Int]
      var r = l
      while (r < n) {
        val x = nums(r)
        val c = cnt.getOrElse(x, 0)
        if (freq.getOrElse(c, 0) > 0) {
          val fc = freq(c) - 1
          if (fc == 0) freq.remove(c)
          else freq(c) = fc
        }
        cnt(x) = c + 1
        freq(cnt(x)) = freq.getOrElse(cnt(x), 0) + 1
        val cx = cnt(x)
        if (
          cnt.size == 1 ||
          (freq.size == 2 && (freq.getOrElse(cx * 2, 0) > 0 || (cx % 2 == 0 && freq.getOrElse(cx / 2, 0) > 0)))
        ) {
          ans = math.max(ans, r - l + 1)
        }
        r += 1
      }
      l += 1
    }
    ans
  }
}
