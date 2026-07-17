// LeetCode 1717 - Maximum Score From Removing Substrings
// https://leetcode.com/problems/maximum-score-from-removing-substrings/

object Solution {
  def maximumGain(s: String, x: Int, y: Int): Int = {
    def remove(text: String, open: Char, close: Char, score: Int): (String, Int) = {
      val stack = new StringBuilder
      var gained = 0
      text.foreach { ch =>
        if (stack.nonEmpty && stack.last == open && ch == close) {
          stack.deleteCharAt(stack.length - 1)
          gained += score
        } else {
          stack.append(ch)
        }
      }
      (stack.toString, gained)
    }

    if (x >= y) {
      val (rest, first) = remove(s, 'a', 'b', x)
      val (_, second) = remove(rest, 'b', 'a', y)
      first + second
    } else {
      val (rest, first) = remove(s, 'b', 'a', y)
      val (_, second) = remove(rest, 'a', 'b', x)
      first + second
    }
  }
}
