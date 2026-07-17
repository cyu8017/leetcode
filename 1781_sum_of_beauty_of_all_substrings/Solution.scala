// LeetCode 1781 - Sum of Beauty of All Substrings
// https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

object Solution {
  def beautySum(s: String): Int = {
    var ans = 0
    for (i <- s.indices) {
      val freq = new Array[Int](26)
      for (j <- i until s.length) {
        freq(s(j) - 'a') += 1
        var lo = Int.MaxValue
        var hi = 0
        for (count <- freq) {
          if (count > 0) {
            lo = math.min(lo, count)
            hi = math.max(hi, count)
          }
        }
        ans += hi - lo
      }
    }
    ans
  }
}
