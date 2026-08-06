// LeetCode 1189 - Maximum Number of Balloons
// https://leetcode.com/problems/maximum-number-of-balloons/

object Solution {
  def maxNumberOfBalloons(text: String): Int = {
    val count = text.groupBy(identity).view.mapValues(_.length).toMap.withDefaultValue(0)
    math.min(count('b'), math.min(count('a'), math.min(count('l') / 2, math.min(count('o') / 2, count('n')))))
  }
}
