// LeetCode 2965 - Find Missing and Repeated Values
// https://leetcode.com/problems/find-missing-and-repeated-values/

object Solution {
  def findMissingAndRepeatedValues(grid: Array[Array[Int]]): Array[Int] = {
    val n = grid.length
    val freq = Array.ofDim[Int](n * n + 1)
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) { freq(grid(i)(j)) += 1; j += 1 }
      i += 1
    }
    var rep = 0
    var miss = 0
    i = 1
    while (i <= n * n) {
      if (freq(i) == 2) rep = i
      if (freq(i) == 0) miss = i
      i += 1
    }
    Array(rep, miss)
  }
}
