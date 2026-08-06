// LeetCode 1598 - Crawler Log Folder
// https://leetcode.com/problems/crawler-log-folder/

object Solution {
  def minOperations(logs: Array[String]): Int = {
    var depth = 0
    for (log <- logs) {
      if (log == "../") depth = math.max(0, depth - 1)
      else if (log != "./") depth += 1
    }
    depth
  }
}
