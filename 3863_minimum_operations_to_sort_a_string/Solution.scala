// LeetCode 3863 - Minimum Operations To Sort A String
// https://leetcode.com/problems/minimum-operations-to-sort-a-string/

object Solution {
  def minOperations(s: String): Int = {
    val n = s.length
    var sorted = true
    var i = 1
    while (i < n) {
      if (s.charAt(i) < s.charAt(i - 1)) { sorted = false; i = n }
      else i += 1
    }
    if (sorted) return 0
    if (n == 2) return -1
    var mn = s.charAt(0)
    var mx = s.charAt(0)
    s.foreach { c =>
      if (c < mn) mn = c
      if (c > mx) mx = c
    }
    if (s.charAt(0) == mn || s.charAt(n - 1) == mx) return 1
    i = 1
    while (i < n - 1) {
      if (s.charAt(i) == mn || s.charAt(i) == mx) return 2
      i += 1
    }
    3
  }
}
