// LeetCode 2027 - Minimum Moves to Convert String
// https://leetcode.com/problems/minimum-moves-to-convert-string/

object Solution {
  def minimumMoves(s: String): Int = {
    var ans = 0
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) == 'X') { ans += 1; i += 3 }
      else i += 1
    }
    ans
  }
}
