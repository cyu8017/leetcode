// LeetCode 0522 - Longest Uncommon Subsequence II
// https://leetcode.com/problems/longest-uncommon-subsequence-ii/

object Solution {
  def findLUSlength(strs: Array[String]): Int = {
    var result = -1
    for (i <- strs.indices) {
      if (!strs.indices.exists(j => i != j && isSubsequence(strs(i), strs(j)))) {
        result = math.max(result, strs(i).length)
      }
    }
    result
  }

  private def isSubsequence(target: String, source: String): Boolean = {
    var index = 0
    for (char <- source if index < target.length && target(index) == char) {
      index += 1
    }
    index == target.length
  }
}
