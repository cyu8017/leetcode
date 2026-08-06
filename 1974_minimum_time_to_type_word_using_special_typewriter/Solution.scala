// LeetCode 1974 - Minimum Time to Type Word Using Special Typewriter
// https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

object Solution {
  def minTimeToType(word: String): Int = {
    var cur = 'a'
    var ans = 0
    for (ch <- word) {
      val d = math.abs(ch - cur)
      ans += math.min(d, 26 - d) + 1
      cur = ch
    }
    ans
  }
}
