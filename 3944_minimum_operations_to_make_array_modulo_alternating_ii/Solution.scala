// LeetCode 3944 - Minimum Operations to Make Array Modulo Alternating II
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-ii/

object Solution {
  def minOperations(nums: Array[Int], k: Int): Long = {
    val evenFreq = new Array[Long](k)
    val oddFreq = new Array[Long](k)
    var i = 0
    while (i < nums.length) {
      if (i % 2 == 0) evenFreq(nums(i) % k) += 1
      else oddFreq(nums(i) % k) += 1
      i += 1
    }
    val evenCost = costs(evenFreq, k)
    val oddCost = costs(oddFreq, k)
    var best1 = 1L << 62
    var best2 = 1L << 62
    var bestIndex = -1
    i = 0
    while (i < k) {
      val x = oddCost(i)
      if (x < best1) {
        best2 = best1
        best1 = x
        bestIndex = i
      } else if (x < best2) best2 = x
      i += 1
    }
    var ans = 1L << 62
    var x = 0
    while (x < k) {
      val other = if (x == bestIndex) best2 else best1
      ans = math.min(ans, evenCost(x) + other)
      x += 1
    }
    ans
  }

  private def costs(freq: Array[Long], k: Int): Array[Long] = {
    val dbl = new Array[Long](2 * k)
    var i = 0
    while (i < 2 * k) {
      dbl(i) = freq(i % k)
      i += 1
    }
    val countPrefix = new Array[Long](2 * k + 1)
    val weightedPrefix = new Array[Long](2 * k + 1)
    i = 0
    while (i < 2 * k) {
      countPrefix(i + 1) = countPrefix(i) + dbl(i)
      weightedPrefix(i + 1) = weightedPrefix(i) + i.toLong * dbl(i)
      i += 1
    }
    val res = new Array[Long](k)
    val cw = k / 2
    val cc = (k - 1) / 2
    var t = 0
    while (t < k) {
      val cnt = countPrefix(t + cw + 1) - countPrefix(t)
      val sum = weightedPrefix(t + cw + 1) - weightedPrefix(t)
      res(t) += sum - t.toLong * cnt
      if (cc > 0) {
        val cnt2 = countPrefix(t + k) - countPrefix(t + k - cc)
        val sum2 = weightedPrefix(t + k) - weightedPrefix(t + k - cc)
        res(t) += (t + k).toLong * cnt2 - sum2
      }
      t += 1
    }
    res
  }
}
