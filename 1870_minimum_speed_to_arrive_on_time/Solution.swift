// LeetCode 1870 - Minimum Speed to Arrive on Time
// https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

class Solution {
    func minSpeedOnTime(_ dist: [Int], _ hour: Double) -> Int {
        let n = dist.count
        if Double(n - 1) >= hour {
            return -1
        }

        func canArrive(_ speed: Int) -> Bool {
            var time = 0.0
            for i in 0..<(n - 1) {
                time += Double((dist[i] + speed - 1) / speed)
            }
            time += Double(dist[n - 1]) / Double(speed)
            return time <= hour
        }

        if !canArrive(10_000_000) {
            return -1
        }

        var lo = 1
        var hi = 10_000_000
        while lo < hi {
            let mid = (lo + hi) / 2
            if canArrive(mid) {
                hi = mid
            } else {
                lo = mid + 1
            }
        }
        return lo
    }
}
