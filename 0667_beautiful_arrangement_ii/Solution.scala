// LeetCode 0667 - Beautiful Arrangement II
// https://leetcode.com/problems/beautiful-arrangement-ii/

object Solution {
  def constructArray(n: Int, k: Int): Array[Int] = {
    val res = Array.fill(n)(0)
    var idx = 0
    var i = 1
    while (i <= n - k) {
      res(idx) = i
      idx += 1
      i += 1
    }
    var left = n - k + 1
    var right = n
    var takeHigh = true
    while (left <= right) {
      if (takeHigh) {
        res(idx) = right
        right -= 1
      } else {
        res(idx) = left
        left += 1
      }
      idx += 1
      takeHigh = !takeHigh
    }
    res
  }
}
