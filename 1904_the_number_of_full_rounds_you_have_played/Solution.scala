// LeetCode 1904 - The Number of Full Rounds You Have Played
// https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/

object Solution {
  def numberOfRounds(loginTime: String, logoutTime: String): Int = {
    def toMin(t: String): Int = {
      val parts = t.split(":")
      parts(0).toInt * 60 + parts(1).toInt
    }
    var start = toMin(loginTime)
    var end = toMin(logoutTime)
    if (end < start) end += 24 * 60
    start = (start + 14) / 15 * 15
    end = end / 15 * 15
    math.max(0, (end - start) / 15)
  }
}
