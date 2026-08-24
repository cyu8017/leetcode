// LeetCode 3763 - Maximum Total Sum With Threshold Constraints
// https://leetcode.com/problems/maximum-total-sum-with-threshold-constraints/

object Solution {
  def maxSum(nums: Array[Int], threshold: Array[Int]): Long = {
    val n = nums.length
    val idx = Array.tabulate[Integer](n)(i => i)
    java.util.Arrays.sort(idx, (a: Integer, b: Integer) => Integer.compare(threshold(a), threshold(b)))
    val tree = new java.util.PriorityQueue[Integer]((a: Integer, b: Integer) => Integer.compare(b, a))
    var ans = 0L
    var i = 0
    var step = 1
    var done = false
    while (!done) {
      while (i < n && threshold(idx(i)) <= step) {
        tree.offer(nums(idx(i)))
        i += 1
      }
      if (tree.isEmpty) done = true
      else {
        ans += tree.poll()
        step += 1
      }
    }
    ans
  }
}
