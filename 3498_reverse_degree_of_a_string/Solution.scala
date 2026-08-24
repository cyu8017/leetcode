// LeetCode 3498 - Reverse Degree of a String
// https://leetcode.com/problems/reverse-degree-of-a-string/

object Solution {
  def reverseDegree(s: String): Int = {
    var ans = 0
    var i = 0
    while (i < s.length) {
      ans += (26 - (s.charAt(i) - 'a')) * (i + 1)
      i += 1
    }
    ans
  }
}
