// LeetCode 0539 - Minimum Time Difference
// https://leetcode.com/problems/minimum-time-difference/

class Solution {
    func findMinDifference(_ timePoints: [String]) -> Int {
        let minutes = timePoints.map { time -> Int in
            let parts = time.split(separator: ":").map { Int($0)! }
            return parts[0] * 60 + parts[1]
        }.sorted()

        var best = minutes.last! - minutes.first!
        for i in 1..<minutes.count {
            best = min(best, minutes[i] - minutes[i - 1])
        }
        return min(best, 24 * 60 - minutes.last! + minutes.first!)
    }
}
