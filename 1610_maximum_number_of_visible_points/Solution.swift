// LeetCode 1610 - Maximum Number of Visible Points
// https://leetcode.com/problems/maximum-number-of-visible-points/

import Foundation

class Solution {
    func visiblePoints(_ points: [[Int]], _ angle: Int, _ location: [Int]) -> Int {
        var same = 0
        var a = [Double]()
        for p in points {
            let dx = Double(p[0] - location[0])
            let dy = Double(p[1] - location[1])
            if dx == 0 && dy == 0 {
                same += 1
            } else {
                a.append(atan2(dy, dx))
            }
        }
        a.sort()
        let ext = a + a.map { $0 + 2 * Double.pi }
        let width = Double(angle) * Double.pi / 180.0 + 1e-12
        var left = 0
        var best = 0
        for right in 0..<ext.count {
            while ext[right] - ext[left] > width {
                left += 1
            }
            best = max(best, min(a.count, right - left + 1))
        }
        return best + same
    }
}
