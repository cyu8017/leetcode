// LeetCode 0955 - Delete Columns to Make Sorted II
// https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

object Solution {
  def minDeletionSize(strs: Array[String]): Int = {
    val n = strs.length
    val m = strs(0).length
    var deleted = 0
    val sortedPair = Array.ofDim[Boolean](n - 1)
    var c = 0
    while (c < m) {
      var bad = false
      var r = 0
      while (r + 1 < n && !bad) {
        if (!sortedPair(r) && strs(r).charAt(c) > strs(r + 1).charAt(c)) bad = true
        r += 1
      }
      if (bad) deleted += 1
      else {
        r = 0
        while (r + 1 < n) {
          if (strs(r).charAt(c) < strs(r + 1).charAt(c)) sortedPair(r) = true
          r += 1
        }
      }
      c += 1
    }
    deleted
  }
}
