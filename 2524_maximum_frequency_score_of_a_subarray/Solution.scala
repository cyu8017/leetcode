// LeetCode 2524 - Maximum Frequency Score of a Subarray
// https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/

object Solution {
  private val MOD = 1000000007

  private def modPow(a0: Long, e0: Long): Long = {
    var res = 1L
    var a = a0 % MOD
    var e = e0
    while (e > 0) {
      if ((e & 1) != 0) res = res * a % MOD
      a = a * a % MOD
      e >>= 1
    }
    res
  }

  def maxFrequencyScore(nums: Array[Int], k: Int): Int = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    var score = 0L
    var best = 0L
    var i = 0
    while (i < nums.length) {
      score = add(freq, score, nums(i))
      if (i >= k) score = remove(freq, score, nums(i - k))
      if (i >= k - 1 && score > best) best = score
      i += 1
    }
    best.toInt
  }

  private def add(freq: scala.collection.mutable.Map[Int, Int], score0: Long, x: Int): Long = {
    var score = score0
    val c = freq.getOrElse(x, 0)
    if (c > 0) score = (score - modPow(x.toLong, c.toLong) + MOD) % MOD
    freq(x) = c + 1
    (score + modPow(x.toLong, (c + 1).toLong)) % MOD
  }

  private def remove(freq: scala.collection.mutable.Map[Int, Int], score0: Long, x: Int): Long = {
    var score = score0
    val c = freq(x)
    score = (score - modPow(x.toLong, c.toLong) + MOD) % MOD
    if (c == 1) freq.remove(x)
    else {
      freq(x) = c - 1
      score = (score + modPow(x.toLong, (c - 1).toLong)) % MOD
    }
    score
  }
}
