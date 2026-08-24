// LeetCode 2902 - Count of Sub-Multisets With Bounded Sum
// https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/

object Solution {
  def countSubMultisets(nums: Array[Int], l: Int, r0: Int): Int = {
    val mod = 1000000007
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    var total = 0
    nums.foreach { v =>
      freq(v) = freq.getOrElse(v, 0) + 1
      total += v
    }
    if (total < l) return 0
    var r = r0
    if (r > total) r = total
    var dp = Array.fill(r + 1)(0)
    dp(0) = 1
    val zeros = freq.getOrElse(0, 0)
    freq.remove(0)
    freq.foreach { case (v, c) =>
      val ndp = Array.fill(r + 1)(0)
      for (sum <- 0 to r if dp(sum) != 0) {
        var k = 0
        while (k <= c && sum + k * v <= r) {
          ndp(sum + k * v) = (ndp(sum + k * v) + dp(sum)) % mod
          k += 1
        }
      }
      dp = ndp
    }
    var ans = 0
    for (s <- l to r) ans = (ans + dp(s)) % mod
    (1L * ans * (zeros + 1) % mod).toInt
  }
}
