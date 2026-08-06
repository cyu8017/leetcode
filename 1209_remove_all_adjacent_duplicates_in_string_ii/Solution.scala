// LeetCode 1209 - Remove All Adjacent Duplicates in String II
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

object Solution {
  def removeDuplicates(s: String, k: Int): String = {
    val stack = scala.collection.mutable.ArrayBuffer.empty[(Char, Int)]
    for (ch <- s) {
      if (stack.nonEmpty && stack.last._1 == ch) {
        val (c, cnt) = stack.remove(stack.length - 1)
        val neu = cnt + 1
        if (neu < k) stack += ((c, neu))
      } else stack += ((ch, 1))
    }
    stack.map { case (c, cnt) => c.toString * cnt }.mkString
  }
}
