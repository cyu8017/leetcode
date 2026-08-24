// LeetCode 0839 - Similar String Groups
// https://leetcode.com/problems/similar-string-groups/

object Solution {
  def numSimilarGroups(strs: Array[String]): Int = {
    val n = strs.length
    val parent = Array.tabulate(n)(identity)
    def find(x0: Int): Int = {
      var x = x0
      while (parent(x) != x) {
        parent(x) = parent(parent(x))
        x = parent(x)
      }
      x
    }
    def similar(a: String, b: String): Boolean = {
      var d0 = -1
      var d1 = -1
      var diffs = 0
      var i = 0
      while (i < a.length) {
        if (a.charAt(i) != b.charAt(i)) {
          diffs += 1
          if (diffs > 2) return false
          if (d0 < 0) d0 = i else d1 = i
        }
        i += 1
      }
      diffs == 0 || (diffs == 2 && a.charAt(d0) == b.charAt(d1) && a.charAt(d1) == b.charAt(d0))
    }
    var groups = n
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        if (similar(strs(i), strs(j))) {
          val pi = find(i)
          val pj = find(j)
          if (pi != pj) {
            parent(pi) = pj
            groups -= 1
          }
        }
        j += 1
      }
      i += 1
    }
    groups
  }
}
