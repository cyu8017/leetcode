// LeetCode 3043 - Find the Length of the Longest Common Prefix
// https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

object Solution {
  def longestCommonPrefix(arr1: Array[Int], arr2: Array[Int]): Int = {
    val s = scala.collection.mutable.HashSet[Int]()
    for (x0 <- arr1) {
      var x = x0
      while (x > 0) { s += x; x /= 10 }
    }
    var mx = 0
    for (x0 <- arr2) {
      var x = x0
      var done = false
      while (x > 0 && !done) {
        if (s.contains(x)) { mx = math.max(mx, x); done = true }
        x /= 10
      }
    }
    if (mx > 0) mx.toString.length else 0
  }
}
