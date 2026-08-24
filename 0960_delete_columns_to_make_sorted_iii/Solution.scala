// LeetCode 0960 - Delete Columns to Make Sorted III
// https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

object Solution {
  def minDeletionSize(strs: Array[String]): Int = {
    val m = strs(0).length
    val dp = Array.fill(m)(1)
    var j = 0
    while (j < m) {
      var i = 0
      while (i < j) {
        var ok = true
        strs.foreach { row => if (row.charAt(i) > row.charAt(j)) ok = false }
        if (ok) dp(j) = math.max(dp(j), dp(i) + 1)
        i += 1
      }
      j += 1
    }
    m - dp.max
  }
}
