// LeetCode 1539 - Kth Missing Positive Number
// https://leetcode.com/problems/kth-missing-positive-number/

object Solution {
  def findKthPositive(arr: Array[Int], k: Int): Int = {
    var left = 0
    var right = arr.length
    while (left < right) {
      val middle = (left + right) / 2
      if (arr(middle) - middle - 1 < k) left = middle + 1
      else right = middle
    }
    left + k
  }
}
