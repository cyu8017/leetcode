// LeetCode 3295 - Report Spam Message
// https://leetcode.com/problems/report-spam-message/

class Solution {
    func reportSpam(_ message: [String], _ bannedWords: [String]) -> Bool {
        let ban = Set(bannedWords)
        var cnt = 0
        for w in message {
            if ban.contains(w) {
                cnt += 1
                if cnt >= 2 { return true }
            }
        }
        return false
    }
}
