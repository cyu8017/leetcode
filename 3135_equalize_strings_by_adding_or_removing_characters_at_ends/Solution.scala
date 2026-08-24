// LeetCode 3135 - Equalize Strings by Adding or Removing Characters at Ends
// https://leetcode.com/problems/equalize-strings-by-adding-or-removing-characters-at-ends/

object Solution {
  def minOperations(initial: String, target: String): Int = {
    val m = initial.length
    val n = target.length
    val f = Array.ofDim[Int](m + 1, n + 1)
    var mx = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (initial.charAt(i) == target.charAt(j)) {
          f(i + 1)(j + 1) = f(i)(j) + 1
          mx = math.max(mx, f(i + 1)(j + 1))
        }
        j += 1
      }
      i += 1
    }
    m + n - 2 * mx
  }
}
