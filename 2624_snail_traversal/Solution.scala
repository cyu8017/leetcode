// LeetCode 2624 - Snail Traversal
// https://leetcode.com/problems/snail-traversal/

object Solution {
  def snail(nums: Array[Int], rowsCount: Int, colsCount: Int): Array[Array[Int]] = {
    if (rowsCount * colsCount != nums.length) return Array.empty[Array[Int]]
    val ans = Array.fill(rowsCount)(Array.fill(colsCount)(0))
    var idx = 0
    var c = 0
    while (c < colsCount) {
      if (c % 2 == 0) {
        var r = 0
        while (r < rowsCount) {
          ans(r)(c) = nums(idx)
          idx += 1
          r += 1
        }
      } else {
        var r = rowsCount - 1
        while (r >= 0) {
          ans(r)(c) = nums(idx)
          idx += 1
          r -= 1
        }
      }
      c += 1
    }
    ans
  }
}
