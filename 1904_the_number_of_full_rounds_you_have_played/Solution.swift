// LeetCode 1904 - The Number of Full Rounds You Have Played
// https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/

class Solution {
    func numberOfRounds(_ loginTime: String, _ logoutTime: String) -> Int {
        func toMin(_ t: String) -> Int {
            let parts = t.split(separator: ":").map { Int($0)! }
            return parts[0] * 60 + parts[1]
        }
        var start = toMin(loginTime)
        var end = toMin(logoutTime)
        if end < start { end += 24 * 60 }
        start = (start + 14) / 15 * 15
        end = end / 15 * 15
        return max(0, (end - start) / 15)
    }
}
