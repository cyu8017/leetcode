// LeetCode 1003 - Check If Word Is Valid After Substitutions
// https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

object Solution {
  def isValid(s: String): Boolean = {
    val stack = scala.collection.mutable.ArrayBuffer.empty[Char]
    for (ch <- s) {
      stack += ch
      if (stack.length >= 3 &&
          stack(stack.length - 3) == 'a' &&
          stack(stack.length - 2) == 'b' &&
          stack(stack.length - 1) == 'c') {
        stack.trimEnd(3)
      }
    }
    stack.isEmpty
  }
}
