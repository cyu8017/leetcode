// LeetCode 1089 - Duplicate Zeros
// https://leetcode.com/problems/duplicate-zeros/

object Solution {
  def duplicateZeros(arr: Array[Int]): Unit = {
    var zeros = arr.count(_ == 0)
    val n = arr.length
    for (i <- n - 1 to 0 by -1) {
      if (i + zeros < n) arr(i + zeros) = arr(i)
      if (arr(i) == 0) {
        zeros -= 1
        if (i + zeros < n) arr(i + zeros) = 0
      }
    }
  }
}
