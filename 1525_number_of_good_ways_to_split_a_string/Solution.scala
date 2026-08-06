// LeetCode 1525 - Number of Good Ways to Split a String
// https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

object Solution {
  def numSplits(s: String): Int = {
    val right = scala.collection.mutable.Map.empty[Char, Int]
    for (ch <- s) right(ch) = right.getOrElse(ch, 0) + 1
    val left = scala.collection.mutable.Set.empty[Char]
    var answer = 0
    for (i <- 0 until s.length - 1) {
      val ch = s(i)
      left += ch
      right(ch) = right(ch) - 1
      if (right(ch) == 0) right.remove(ch)
      if (left.size == right.size) answer += 1
    }
    answer
  }
}
