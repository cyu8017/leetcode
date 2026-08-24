// LeetCode 3853 - Merge Close Characters
// https://leetcode.com/problems/merge-close-characters/

object Solution {
  def mergeCharacters(s: String, k: Int): String = {
    val last = scala.collection.mutable.Map.empty[Char, Int]
    val ans = new StringBuilder
    s.foreach { c =>
      val cur = ans.length
      if (!(last.contains(c) && cur - last(c) <= k)) {
        ans.append(c)
        last(c) = cur
      }
    }
    ans.toString
  }
}
