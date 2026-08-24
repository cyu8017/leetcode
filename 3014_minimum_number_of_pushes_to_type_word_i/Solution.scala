// LeetCode 3014 - Minimum Number of Pushes to Type Word I
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

object Solution {
  def minimumPushes(word: String): Int = {
    val n = word.length
    var ans = 0
    var k = 1
    var i = 0
    while (i < n / 8) {
      ans += k * 8
      k += 1
      i += 1
    }
    ans += k * (n % 8)
    ans
  }
}
