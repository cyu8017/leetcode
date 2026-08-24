// LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen
// https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

object Solution {
  def stringSequence(target: String): Array[String] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[String]
    val cur = new StringBuilder
    for (ch <- target) {
      cur.append('a')
      ans += cur.toString
      while (cur.charAt(cur.length - 1) != ch) {
        cur.setCharAt(cur.length - 1, (cur.charAt(cur.length - 1) + 1).toChar)
        ans += cur.toString
      }
    }
    ans.toArray
  }
}
