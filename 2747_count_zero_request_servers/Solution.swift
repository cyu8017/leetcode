// LeetCode 2747 - Count Zero Request Servers
// https://leetcode.com/problems/count-zero-request-servers/

class Solution {
    func countServers(_ n: Int, _ logs: [[Int]], _ x: Int, _ queries: [Int]) -> [Int] {
        let logs = logs.sorted { $0[1] < $1[1] }
        var qs = queries.enumerated().map { [$1, $0] }
        qs.sort { $0[0] < $1[0] }
        var ans = Array(repeating: 0, count: queries.count)
        var cnt: [Int: Int] = [:]
        var active = 0, l = 0, r = 0
        for q in qs {
            let t = q[0], qi = q[1]
            while r < logs.count && logs[r][1] <= t {
                let id = logs[r][0]
                if cnt[id, default: 0] == 0 { active += 1 }
                cnt[id, default: 0] += 1
                r += 1
            }
            while l < r && logs[l][1] < t - x {
                let id = logs[l][0]
                cnt[id]! -= 1
                if cnt[id] == 0 { active -= 1 }
                l += 1
            }
            ans[qi] = n - active
        }
        return ans
    }
}
