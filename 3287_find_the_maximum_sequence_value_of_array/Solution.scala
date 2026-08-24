// LeetCode 3287 - Find the Maximum Sequence Value of Array
// https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/

object Solution {
  def maxValue(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val MAX = 128
    val left = Array.ofDim[Boolean](n + 1, k + 1, MAX)
    left(0)(0)(0) = true
    var i = 0
    while (i < n) {
      var j = 0
      while (j <= k) {
        var v = 0
        while (v < MAX) {
          if (left(i)(j)(v)) {
            left(i + 1)(j)(v) = true
            if (j < k) left(i + 1)(j + 1)(v | nums(i)) = true
          }
          v += 1
        }
        j += 1
      }
      i += 1
    }
    val right = Array.ofDim[Boolean](n + 1, k + 1, MAX)
    right(n)(0)(0) = true
    i = n - 1
    while (i >= 0) {
      var j = 0
      while (j <= k) {
        var v = 0
        while (v < MAX) {
          if (right(i + 1)(j)(v)) {
            right(i)(j)(v) = true
            if (j < k) right(i)(j + 1)(v | nums(i)) = true
          }
          v += 1
        }
        j += 1
      }
      i -= 1
    }
    var ans = 0
    var mid = k
    while (mid + k <= n) {
      var a = 0
      while (a < MAX) {
        if (left(mid)(k)(a)) {
          var b = 0
          while (b < MAX) {
            if (right(mid)(k)(b) && (a ^ b) > ans) ans = a ^ b
            b += 1
          }
        }
        a += 1
      }
      mid += 1
    }
    ans
  }
}
