// LeetCode 2054 - Two Best Non-Overlapping Events
// https://leetcode.com/problems/two-best-non-overlapping-events/

class Solution {
    func maxTwoEvents(_ events: [[Int]]) -> Int {
        let events = events.sorted { $0[0] < $1[0] }
        let n = events.count
        var suffix = [Int](repeating: 0, count: n + 1)
        for i in stride(from: n - 1, through: 0, by: -1) {
            suffix[i] = max(suffix[i + 1], events[i][2])
        }
        var ans = 0
        for i in 0..<n {
            ans = max(ans, events[i][2])
            var lo = i + 1, hi = n
            while lo < hi {
                let mid = (lo + hi) / 2
                if events[mid][0] > events[i][1] { hi = mid }
                else { lo = mid + 1 }
            }
            if lo < n { ans = max(ans, events[i][2] + suffix[lo]) }
        }
        return ans
    }
}
