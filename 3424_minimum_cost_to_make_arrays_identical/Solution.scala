// LeetCode 3424 - Minimum Cost to Make Arrays Identical
// https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/

object Solution {
  def minCost(arr: Array[Int], brr: Array[Int], k: Long): Long = {
    var noSwap = 0L
    var i = 0
    while (i < arr.length) {
      noSwap += math.abs(arr(i) - brr(i))
      i += 1
    }
    java.util.Arrays.sort(arr)
    java.util.Arrays.sort(brr)
    var withSwap = k
    i = 0
    while (i < arr.length) {
      withSwap += math.abs(arr(i) - brr(i))
      i += 1
    }
    if (noSwap < withSwap) noSwap else withSwap
  }
}
