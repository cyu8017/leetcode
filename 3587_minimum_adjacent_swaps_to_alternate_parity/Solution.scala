// LeetCode 3587 - Minimum Adjacent Swaps to Alternate Parity
// https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/

object Solution {
  def calc(pos: Array[java.util.ArrayList[Integer]], n: Int, k: Int): Int = {
    var res = 0
    var i = 0
    while (i < n) {
      res += math.abs(pos(k).get(i / 2) - i)
      i += 2
    }
    res
  }

  def minSwaps(nums: Array[Int]): Int = {
    val pos = Array(new java.util.ArrayList[Integer](), new java.util.ArrayList[Integer]())
    var i = 0
    while (i < nums.length) { pos(nums(i) & 1).add(i); i += 1 }
    if (math.abs(pos(0).size() - pos(1).size()) > 1) return -1
    if (pos(0).size() > pos(1).size()) return calc(pos, nums.length, 0)
    if (pos(0).size() < pos(1).size()) return calc(pos, nums.length, 1)
    math.min(calc(pos, nums.length, 0), calc(pos, nums.length, 1))
  }
}
