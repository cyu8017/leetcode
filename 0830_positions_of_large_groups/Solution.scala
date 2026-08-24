// LeetCode 0830 - Positions of Large Groups
// https://leetcode.com/problems/positions-of-large-groups/

object Solution {
  def largeGroupPositions(s: String): List[List[Int]] = {
    val ans = scala.collection.mutable.ListBuffer.empty[List[Int]]
    val n = s.length
    var i = 0
    while (i < n) {
      var j = i
      while (j < n && s.charAt(j) == s.charAt(i)) j += 1
      if (j - i >= 3) ans += List(i, j - 1)
      i = j
    }
    ans.toList
  }
}
