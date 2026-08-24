// LeetCode 3671 - Sum of Beautiful Subsequences
// https://leetcode.com/problems/sum-of-beautiful-subsequences/

object Solution {
  def totalBeauty(nums: Array[Int]): Int = {
    val MOD = 1000000007
    var mx = 0
    for (v <- nums) if (v > mx) mx = v
    val pos = Array.fill(mx + 1)(new java.util.ArrayList[Integer]())
    var i = 0
    while (i < nums.length) {
      pos(nums(i)).add(i)
      i += 1
    }
    val cnt = new Array[Int](mx + 1)
    var g = 1
    while (g <= mx) {
      val seq = new java.util.ArrayList[Integer]()
      var m = g
      while (m <= mx) {
        seq.addAll(pos(m))
        m += g
      }
      if (!seq.isEmpty) {
        java.util.Collections.sort(seq)
        var ways = 1
        i = 0
        while (i < seq.size()) {
          ways = ((ways * 2L) % MOD).toInt
          i += 1
        }
        cnt(g) = (ways - 1 + MOD) % MOD
      }
      g += 1
    }
    var ans = 0
    g = mx
    while (g >= 1) {
      var m = 2 * g
      while (m <= mx) {
        cnt(g) = (cnt(g) - cnt(m) + MOD) % MOD
        m += g
      }
      ans = ((ans + 1L * cnt(g) * g) % MOD).toInt
      g -= 1
    }
    ans
  }
}
