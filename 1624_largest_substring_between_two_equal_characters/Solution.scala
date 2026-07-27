// LeetCode 1624 - Largest Substring Between Two Equal Characters
// https://leetcode.com/problems/largest-substring-between-two-equal-characters/

object Solution {
  def maxLengthBetweenEqualCharacters(s: String): Int = {
    val first = scala.collection.mutable.Map.empty[Char, Int]
    var ans = -1
    s.zipWithIndex.foreach { case (ch, i) =>
      if (first.contains(ch)) ans = math.max(ans, i - first(ch) - 1)
      else first(ch) = i
    }
    ans
  }
}
