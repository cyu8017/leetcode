// LeetCode 3433 - Count Mentions Per User
// https://leetcode.com/problems/count-mentions-per-user/

class Solution {
    func countMentions(_ numberOfUsers: Int, _ events: [[String]]) -> [Int] {
        var events = events
        events.sort { a, b in
            let ti = Int(a[1])!, tj = Int(b[1])!
            if ti != tj { return ti < tj }
            return a[0] > b[0]
        }
        var online = Array(repeating: true, count: numberOfUsers)
        var offlineUntil = Array(repeating: 0, count: numberOfUsers)
        var ans = Array(repeating: 0, count: numberOfUsers)
        for e in events {
            let t = Int(e[1])!
            for i in 0..<numberOfUsers {
                if !online[i] && offlineUntil[i] <= t { online[i] = true }
            }
            if e[0] == "OFFLINE" {
                let id = Int(e[2])!
                online[id] = false
                offlineUntil[id] = t + 60
            } else {
                let msg = e[2]
                if msg == "ALL" {
                    for i in 0..<numberOfUsers { ans[i] += 1 }
                } else if msg == "HERE" {
                    for i in 0..<numberOfUsers where online[i] { ans[i] += 1 }
                } else {
                    for part in msg.split(separator: " ") {
                        let id = Int(part.dropFirst(2))!
                        ans[id] += 1
                    }
                }
            }
        }
        return ans
    }
}
