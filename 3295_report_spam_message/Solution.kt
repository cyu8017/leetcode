// LeetCode 3295 - Report Spam Message
// https://leetcode.com/problems/report-spam-message/

class Solution {
    fun reportSpam(message: Array<String>, bannedWords: Array<String>): Boolean {
        val ban = bannedWords.toHashSet()
        var cnt = 0
        for (w in message) {
            if (w in ban) {
                cnt++
                if (cnt >= 2) return true
            }
        }
        return false
    }
}
