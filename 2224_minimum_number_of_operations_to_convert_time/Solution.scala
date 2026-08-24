// LeetCode 2224 - Minimum Number of Operations to Convert Time
// https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

object Solution {
  def convertTime(current: String, correct: String): Int = {
    def toMin(t: String): Int =
      (t.charAt(0) - '0') * 600 + (t.charAt(1) - '0') * 60 +
        (t.charAt(3) - '0') * 10 + (t.charAt(4) - '0')
    var diff = toMin(correct) - toMin(current)
    var ans = 0
    for (step <- Array(60, 15, 5, 1)) {
      ans += diff / step
      diff %= step
    }
    ans
  }
}
