// LeetCode 3637 - Trionic Array I
// https://leetcode.com/problems/trionic-array-i/

object Solution {
  def isTrionic(nums: Array[Int]): Boolean = {
    val n = nums.length
    var p = 0
    while (p < n - 2 && nums(p) < nums(p + 1)) p += 1
    if (p == 0) return false
    var q = p
    while (q < n - 1 && nums(q) > nums(q + 1)) q += 1
    if (q == p || q == n - 1) return false
    while (q < n - 1 && nums(q) < nums(q + 1)) q += 1
    q == n - 1
  }
}
