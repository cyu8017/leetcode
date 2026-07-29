// LeetCode 1055 - Shortest Way to Form String
// https://leetcode.com/problems/shortest-way-to-form-string/

object Solution {
  def shortestWay(source: String, target: String): Int = {
    val sourceSet = source.toSet
    if (target.exists(ch => !sourceSet.contains(ch))) return -1
    var ans = 0
    var i = 0
    val n = target.length
    while (i < n) {
      ans += 1
      for (ch <- source if i < n && target(i) == ch) i += 1
    }
    ans
  }
}
