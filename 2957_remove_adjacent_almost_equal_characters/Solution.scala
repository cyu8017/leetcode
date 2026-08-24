// LeetCode 2957 - Remove Adjacent Almost-Equal Characters
// https://leetcode.com/problems/remove-adjacent-almost-equal-characters/

object Solution {
  def removeAlmostEqualCharacters(word: String): Int = {
    var ans = 0
    val n = word.length
    var i = 1
    while (i < n) {
      if (math.abs(word.charAt(i) - word.charAt(i - 1)) <= 1) {
        ans += 1
        i += 2
      } else i += 1
    }
    ans
  }
}
