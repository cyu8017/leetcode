// LeetCode 3152 - Special Array II
// https://leetcode.com/problems/special-array-ii/

object Solution {
  def isArraySpecial(nums: Array[Int], queries: Array[Array[Int]]): Array[Boolean] = {
    val n = nums.length
    val d = Array.tabulate(n)(i => i)
    var i = 1
    while (i < n) {
      if (nums(i) % 2 != nums(i - 1) % 2) d(i) = d(i - 1)
      i += 1
    }
    Array.tabulate(queries.length)(i => d(queries(i)(1)) <= queries(i)(0))
  }
}
