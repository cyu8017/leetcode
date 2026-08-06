// LeetCode 1200 - Minimum Absolute Difference
// https://leetcode.com/problems/minimum-absolute-difference/

object Solution {
  def minimumAbsDifference(arr: Array[Int]): List[List[Int]] = {
    val sorted = arr.sorted
    val best = (0 until sorted.length - 1).map(i => sorted(i + 1) - sorted(i)).min
    (0 until sorted.length - 1).collect {
      case i if sorted(i + 1) - sorted(i) == best => List(sorted(i), sorted(i + 1))
    }.toList
  }
}
