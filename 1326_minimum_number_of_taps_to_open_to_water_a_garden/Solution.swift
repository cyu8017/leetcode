// LeetCode 1326 - Minimum Number of Taps to Open to Water a Garden
// https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

class Solution {
    func minTaps(_ n: Int, _ ranges: [Int]) -> Int {
        var farthest = Array(repeating: 0, count: n + 1)
        for (center, radius) in ranges.enumerated() {
            let left = max(0, center - radius), right = min(n, center + radius)
            farthest[left] = max(farthest[left], right)
        }
        var taps = 0, end = 0, reach = 0
        for position in 0..<n {
            reach = max(reach, farthest[position])
            if position == end {
                if reach <= position { return -1 }
                taps += 1
                end = reach
            }
        }
        return taps
    }
}
