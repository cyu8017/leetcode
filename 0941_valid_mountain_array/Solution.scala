// LeetCode 0941 - Valid Mountain Array
// https://leetcode.com/problems/valid-mountain-array/

object Solution {
  def validMountainArray(arr: Array[Int]): Boolean = {
    val n = arr.length
    if (n < 3) return false
    var i = 0
    while (i + 1 < n && arr(i) < arr(i + 1)) i += 1
    if (i == 0 || i == n - 1) return false
    while (i + 1 < n && arr(i) > arr(i + 1)) i += 1
    i == n - 1
  }
}
