// LeetCode 1681 - Minimum Incompatibility
// https://leetcode.com/problems/minimum-incompatibility/

object Solution {
  def minimumIncompatibility(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val size = n / k
    val full = (1 << n) - 1
    val groups = scala.collection.mutable.Map.empty[Int, Int]
    for (mask <- 0 until (1 << n) if Integer.bitCount(mask) == size) {
      val seen = scala.collection.mutable.Set[Int]()
      var ok = true
      var mn = Int.MaxValue
      var mx = 0
      var count = 0
      var i = 0
      while (i < n && ok) {
        if (((mask >> i) & 1) == 1) {
          val v = nums(i)
          if (seen.contains(v)) ok = false
          else {
            seen += v
            count += 1
            if (v < mn) mn = v
            if (v > mx) mx = v
          }
        }
        i += 1
      }
      if (ok && count == size) groups(mask) = mx - mn
    }
    val inf = 1000000000
    val memo = scala.collection.mutable.Map.empty[Int, Int]
    def dp(mask: Int): Int = {
      if (mask == full) return 0
      if (memo.contains(mask)) return memo(mask)
      var first = 0
      var i = 0
      while (i < n) {
        if (((mask >> i) & 1) == 0) { first = i; i = n }
        else i += 1
      }
      var best = inf
      for ((g, c) <- groups if ((g >> first) & 1) != 0 && (g & mask) == 0) {
        best = math.min(best, c + dp(mask | g))
      }
      memo(mask) = best
      best
    }
    val ans = dp(0)
    if (ans >= inf) -1 else ans
  }
}
