// LeetCode 0774 - Minimize Max Distance to Gas Station
// https://leetcode.com/problems/minimize-max-distance-to-gas-station/

class Solution {
    func minmaxGasDist(_ stations: [Int], _ k: Int) -> Double {
        var lo = 0.0, hi = Double(stations.last! - stations[0])
        while hi - lo > 1e-6 {
            let mid = (lo + hi) / 2.0
            if can(stations, k, mid) { hi = mid } else { lo = mid }
        }
        return hi
    }

    private func can(_ stations: [Int], _ k: Int, _ dist: Double) -> Bool {
        var needed = 0
        for i in 1..<stations.count {
            needed += Int(Double(stations[i] - stations[i - 1]) / dist)
        }
        return needed <= k
    }
}
