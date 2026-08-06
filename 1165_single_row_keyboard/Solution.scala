// LeetCode 1165 - Single-Row Keyboard
// https://leetcode.com/problems/single-row-keyboard/

object Solution {
  def calculateTime(keyboard: String, word: String): Int = {
    val pos = keyboard.zipWithIndex.toMap
    var ans = 0
    var prev = 0
    for (ch <- word) {
      ans += math.abs(pos(ch) - prev)
      prev = pos(ch)
    }
    ans
  }
}
