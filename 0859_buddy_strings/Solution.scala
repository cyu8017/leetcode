// LeetCode 0859 - Buddy Strings
// https://leetcode.com/problems/buddy-strings/

object Solution {
  def buddyStrings(s: String, goal: String): Boolean = {
    if (s.length != goal.length) return false
    if (s == goal) {
      val seen = scala.collection.mutable.Set.empty[Char]
      s.foreach { ch => if (!seen.add(ch)) return true }
      return false
    }
    val diffs = scala.collection.mutable.ListBuffer.empty[(Char, Char)]
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) != goal.charAt(i)) diffs += ((s.charAt(i), goal.charAt(i)))
      i += 1
    }
    diffs.length == 2 && diffs(0)._1 == diffs(1)._2 && diffs(0)._2 == diffs(1)._1
  }
}
