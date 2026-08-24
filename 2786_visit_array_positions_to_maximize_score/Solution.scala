// LeetCode 2786 - Visit Array Positions to Maximize Score
// https://leetcode.com/problems/visit-array-positions-to-maximize-score/

object Solution {
  def maxScore(nums: Array[Int], x: Int): Long = {
    val NEG = -(1L << 60)
    var even = nums(0).toLong
    var odd = nums(0).toLong
    if (nums(0) % 2 == 0) odd = NEG
    else even = NEG
    var i = 1
    while (i < nums.length) {
      val v = nums(i).toLong
      if (nums(i) % 2 == 0) even = math.max(even + v, odd + v - x)
      else odd = math.max(odd + v, even + v - x)
      i += 1
    }
    math.max(even, odd)
  }
}
