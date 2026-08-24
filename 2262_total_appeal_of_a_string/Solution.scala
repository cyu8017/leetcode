// LeetCode 2262 - Total Appeal of A String
// https://leetcode.com/problems/total-appeal-of-a-string/

object Solution {
  def appealSum(s: String): Long = {
    val last = Array.fill(26)(-1)
    var ans = 0L
    var cur = 0L
    var i = 0
    while (i < s.length) {
      val c = s.charAt(i) - 'a'
      cur += i - last(c)
      last(c) = i
      ans += cur
      i += 1
    }
    ans
  }
}
