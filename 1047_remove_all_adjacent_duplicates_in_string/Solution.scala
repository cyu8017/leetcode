// LeetCode 1047 - Remove All Adjacent Duplicates In String
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

object Solution {
  def removeDuplicates(s: String): String = {
    val stack = scala.collection.mutable.ArrayBuffer.empty[Char]
    for (ch <- s) {
      if (stack.nonEmpty && stack.last == ch) stack.remove(stack.length - 1)
      else stack += ch
    }
    stack.mkString
  }
}
