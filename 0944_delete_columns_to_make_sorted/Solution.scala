// LeetCode 0944 - Delete Columns to Make Sorted
// https://leetcode.com/problems/delete-columns-to-make-sorted/

object Solution {
  def minDeletionSize(strs: Array[String]): Int = {
    var ans = 0
    val m = strs(0).length
    val n = strs.length
    var c = 0
    while (c < m) {
      var r = 0
      var bad = false
      while (r + 1 < n && !bad) {
        if (strs(r).charAt(c) > strs(r + 1).charAt(c)) { ans += 1; bad = true }
        r += 1
      }
      c += 1
    }
    ans
  }
}
