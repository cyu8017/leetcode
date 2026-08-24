// LeetCode 3295 - Report Spam Message
// https://leetcode.com/problems/report-spam-message/

object Solution {
  def reportSpam(message: Array[String], bannedWords: Array[String]): Boolean = {
    val ban = bannedWords.toSet
    var cnt = 0
    for (w <- message) {
      if (ban.contains(w)) {
        cnt += 1
        if (cnt >= 2) return true
      }
    }
    false
  }
}
