// LeetCode 1544 - Make The String Great
// https://leetcode.com/problems/make-the-string-great/

object Solution {
  def makeGood(s: String): String = {
    val stack = scala.collection.mutable.ArrayBuffer.empty[Char]
    for (ch <- s) {
      if (stack.nonEmpty && stack.last != ch && stack.last.toLower == ch.toLower) stack.remove(stack.length - 1)
      else stack += ch
    }
    stack.mkString
  }
}
