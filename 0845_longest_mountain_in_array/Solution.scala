// LeetCode 0845 - Longest Mountain in Array
// https://leetcode.com/problems/longest-mountain-in-array/

object Solution {
  def longestMountain(arr: Array[Int]): Int = {
    val n = arr.length
    var ans = 0
    var i = 0
    while (i < n) {
      var j = i
      if (j + 1 < n && arr(j) < arr(j + 1)) {
        while (j + 1 < n && arr(j) < arr(j + 1)) j += 1
        if (j + 1 < n && arr(j) > arr(j + 1)) {
          while (j + 1 < n && arr(j) > arr(j + 1)) j += 1
          ans = math.max(ans, j - i + 1)
          i = j
        } else i += 1
      } else i += 1
    }
    ans
  }
}
