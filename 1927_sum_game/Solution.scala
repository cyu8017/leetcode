// LeetCode 1927 - Sum Game
// https://leetcode.com/problems/sum-game/

object Solution {
  def sumGame(num: String): Boolean = {
    val half = num.length / 2
    def score(s: String): Int = {
      var q = 0
      var dig = 0
      for (c <- s) {
        if (c == '?') q += 1
        else dig += c - '0'
      }
      dig * 2 + q * 9
    }
    score(num.substring(0, half)) != score(num.substring(half))
  }
}
