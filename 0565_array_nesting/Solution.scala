// LeetCode 0565 - Array Nesting
// https://leetcode.com/problems/array-nesting/

object Solution {
  def arrayNesting(nums: Array[Int]): Int = {
    var best = 0
    var i = 0
    while (i < nums.length) {
      if (nums(i) >= 0) {
        var length = 0
        var j = i
        while (nums(j) >= 0) {
          val nxt = nums(j)
          nums(j) = -1
          j = nxt
          length += 1
        }
        best = math.max(best, length)
      }
      i += 1
    }
    best
  }
}
