// LeetCode 0777 - Swap Adjacent in LR String
// https://leetcode.com/problems/swap-adjacent-in-lr-string/

object Solution {
  def canTransform(start: String, result: String): Boolean = {
    val a = new StringBuilder
    val b = new StringBuilder
    for (ch <- start if ch != 'X') a.append(ch)
    for (ch <- result if ch != 'X') b.append(ch)
    if (a.toString != b.toString) return false
    var i = 0
    var j = 0
    val n = start.length
    while (i < n && j < n) {
      while (i < n && start.charAt(i) == 'X') i += 1
      while (j < n && result.charAt(j) == 'X') j += 1
      if (i == n || j == n) return true
      if (start.charAt(i) != result.charAt(j)) return false
      if (start.charAt(i) == 'L' && i < j) return false
      if (start.charAt(i) == 'R' && i > j) return false
      i += 1
      j += 1
    }
    true
  }
}
