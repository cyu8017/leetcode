// LeetCode 2345 - Finding the Number of Visible Mountains
// https://leetcode.com/problems/finding-the-number-of-visible-mountains/

object Solution {
  def visibleMountains(peaks: Array[Array[Int]]): Int = {
    val arr = peaks.map(p => Array(p(0) - p(1), p(0) + p(1)))
    scala.util.Sorting.stableSort(arr, (a: Array[Int], b: Array[Int]) => {
      if (a(0) == b(0)) a(1) > b(1) else a(0) < b(0)
    })
    var ans = 0
    var maxR = Int.MinValue
    var i = 0
    while (i < arr.length) {
      var j = i
      while (j < arr.length && arr(j)(0) == arr(i)(0) && arr(j)(1) == arr(i)(1)) j += 1
      if (arr(i)(1) > maxR) {
        if (j - i == 1) ans += 1
        maxR = arr(i)(1)
      }
      i = j
    }
    ans
  }
}
