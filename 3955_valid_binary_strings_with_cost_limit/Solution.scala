// LeetCode 3955 - Valid Binary Strings With Cost Limit
// https://leetcode.com/problems/valid-binary-strings-with-cost-limit/

import scala.collection.mutable

object Solution {
  def generateValidStrings(n: Int, k: Int): List[String] = {
    val ans = mutable.ArrayBuffer.empty[String]
    val path = new StringBuilder()
    dfs(0, 0, n, k, path, ans)
    ans.toList
  }

  private def dfs(i: Int, tot: Int, n: Int, k: Int, path: StringBuilder, ans: mutable.ArrayBuffer[String]): Unit = {
    if (i >= n) {
      ans += path.toString
      return
    }
    path.append('0')
    dfs(i + 1, tot, n, k, path, ans)
    path.deleteCharAt(path.length - 1)
    if ((path.length == 0 || path.charAt(path.length - 1) == '0') && tot + i <= k) {
      path.append('1')
      dfs(i + 1, tot + i, n, k, path, ans)
      path.deleteCharAt(path.length - 1)
    }
  }
}
