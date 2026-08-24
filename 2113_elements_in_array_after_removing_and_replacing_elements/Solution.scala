// LeetCode 2113 - Elements in Array After Removing and Replacing Elements
// https://leetcode.com/problems/elements-in-array-after-removing-and-replacing-elements/

object Solution {
  def elementInNums(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val n = nums.length
    val ans = Array.fill(queries.length)(0)
    var i = 0
    while (i < queries.length) {
      val t = queries(i)(0)
      val idx = queries(i)(1)
      val cycle = t % (2 * n)
      val (size, offset) =
        if (cycle < n) (n - cycle, cycle)
        else (cycle - n, 0)
      ans(i) = if (idx >= size) -1 else nums(offset + idx)
      i += 1
    }
    ans
  }
}
