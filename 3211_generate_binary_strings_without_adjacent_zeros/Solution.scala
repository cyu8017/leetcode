// LeetCode 3211 - Generate Binary Strings Without Adjacent Zeros
// https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/

object Solution {
  def validStrings(n: Int): List[String] = {
    val ans = scala.collection.mutable.ListBuffer.empty[String]
    val t = new StringBuilder
    def dfs(i: Int): Unit = {
      if (i >= n) { ans += t.toString; return }
      var j = 0
      while (j < 2) {
        if ((j == 0 && (i == 0 || t.charAt(i - 1) == '1')) || j == 1) {
          t.append(('0' + j).toChar)
          dfs(i + 1)
          t.deleteCharAt(t.length - 1)
        }
        j += 1
      }
    }
    dfs(0)
    ans.toList
  }
}
