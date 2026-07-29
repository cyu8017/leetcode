// LeetCode 1081 - Smallest Subsequence of Distinct Characters
// https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

object Solution {
  def smallestSubsequence(s: String): String = {
    val last = s.zipWithIndex.groupBy(_._1).map { case (ch, pairs) => ch -> pairs.map(_._2).max }
    val stack = scala.collection.mutable.ArrayBuffer.empty[Char]
    val used = scala.collection.mutable.Set.empty[Char]
    for (i <- s.indices) {
      val ch = s(i)
      if (!used.contains(ch)) {
        while (stack.nonEmpty && ch < stack.last && last(stack.last) > i) {
          used -= stack.remove(stack.length - 1)
        }
        stack += ch
        used += ch
      }
    }
    stack.mkString
  }
}
