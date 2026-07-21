// LeetCode 1883 - Minimum Skips to Arrive at Meeting On Time
// https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/

class Solution {
    func minSkips(_ dist: [Int], _ speed: Int, _ hoursBefore: Int) -> Int {
        let limit = hoursBefore * speed
        let n = dist.count
        var dp = Array(repeating: Int.max, count: n + 1)
        dp[0] = 0

        for road in dist {
            var nxt = Array(repeating: Int.max, count: n + 1)
            for skips in 0..<n {
                if dp[skips] == Int.max {
                    continue
                }
                let withRest = ((dp[skips] + road + speed - 1) / speed) * speed
                nxt[skips] = min(nxt[skips], withRest)
                nxt[skips + 1] = min(nxt[skips + 1], dp[skips] + road)
            }
            dp = nxt
        }

        for skips in 0...n {
            if dp[skips] <= limit {
                return skips
            }
        }
        return -1
    }
}
