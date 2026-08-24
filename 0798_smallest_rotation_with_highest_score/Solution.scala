// LeetCode 0798 - Smallest Rotation with Highest Score
// https://leetcode.com/problems/smallest-rotation-with-highest-score/

object Solution {
  def bestRotation(nums: Array[Int]): Int = {
    val n = nums.length
    val change = Array.fill(n)(1)
    var i = 0
    while (i < n) {
      change((i - nums(i) + 1 + n) % n) -= 1
      i += 1
    }
    i = 1
    while (i < n) {
      change(i) += change(i - 1)
      i += 1
    }
    var best = 0
    i = 1
    while (i < n) {
      if (change(i) > change(best)) best = i
      i += 1
    }
    best
  }
}
