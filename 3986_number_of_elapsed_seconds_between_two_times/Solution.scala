// LeetCode 3986 - Number of Elapsed Seconds Between Two Times
// https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/

object Solution {
  private def toSeconds(s: String): Int = {
    val h = (s.charAt(0) - '0') * 10 + (s.charAt(1) - '0')
    val m = (s.charAt(3) - '0') * 10 + (s.charAt(4) - '0')
    val sec = (s.charAt(6) - '0') * 10 + (s.charAt(7) - '0')
    h * 3600 + m * 60 + sec
  }

  def secondsBetweenTimes(startTime: String, endTime: String): Int =
    toSeconds(endTime) - toSeconds(startTime)
}
