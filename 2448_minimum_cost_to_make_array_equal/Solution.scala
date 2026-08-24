// LeetCode 2448 - Minimum Cost to Make Array Equal
// https://leetcode.com/problems/minimum-cost-to-make-array-equal/

object Solution {
  def minCost(nums: Array[Int], cost: Array[Int]): Long = {
    val n = nums.length
    val idx = Array.tabulate(n)(identity)
    scala.util.Sorting.stableSort(idx, (a: Int, b: Int) => nums(a) < nums(b) || (nums(a) == nums(b) && a < b))
    var totalCost = 0L
    var i = 0
    while (i < n) { totalCost += cost(i); i += 1 }
    var pref = 0L
    var median = 0
    i = 0
    var found = false
    while (i < n && !found) {
      pref += cost(idx(i))
      if (pref * 2 >= totalCost) {
        median = nums(idx(i))
        found = true
      }
      i += 1
    }
    var ans = 0L
    i = 0
    while (i < n) {
      var diff = nums(i).toLong - median
      if (diff < 0) diff = -diff
      ans += diff * cost(i)
      i += 1
    }
    ans
  }
}
