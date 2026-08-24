// LeetCode 3468 - Find the Number of Copy Arrays
// https://leetcode.com/problems/find-the-number-of-copy-arrays/

object Solution {
  def countArrays(original: Array[Int], bounds: Array[Array[Int]]): Int = {
    val n = original.length
    var lo = bounds(0)(0)
    var hi = bounds(0)(1)
    var i = 1
    while (i < n) {
      val diff = original(i) - original(i - 1)
      val lo2 = bounds(i)(0)
      val hi2 = bounds(i)(1)
      var nlo = lo + diff
      var nhi = hi + diff
      if (nlo < lo2) nlo = lo2
      if (nhi > hi2) nhi = hi2
      if (nlo > nhi) return 0
      lo = nlo
      hi = nhi
      i += 1
    }
    hi - lo + 1
  }
}
