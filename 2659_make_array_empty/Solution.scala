// LeetCode 2659 - Make Array Empty
// https://leetcode.com/problems/make-array-empty/

object Solution {
  def countOperationsToEmptyArray(nums: Array[Int]): Long = {
    val n = nums.length
    val idx = Array.tabulate(n)(identity)
    val sorted = idx.sortBy(nums)
    var ans = n.toLong
    var i = 1
    while (i < n) {
      if (sorted(i) < sorted(i - 1)) ans += n - i
      i += 1
    }
    ans
  }
}
