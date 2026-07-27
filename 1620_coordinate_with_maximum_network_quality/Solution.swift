// LeetCode 1620 - Coordinate With Maximum Network Quality
// https://leetcode.com/problems/coordinate-with-maximum-network-quality/

import Foundation

class Solution {
    func bestCoordinate(_ towers: [[Int]], _ radius: Int) -> [Int] {
        var best = [0, 0]
        var quality = -1
        for x in 0...50 {
            for y in 0...50 {
                var q = 0
                for t in towers {
                    let d = hypot(Double(x - t[0]), Double(y - t[1]))
                    if d <= Double(radius) {
                        q += Int(Double(t[2]) / (1.0 + d))
                    }
                }
                if q > quality {
                    quality = q
                    best = [x, y]
                }
            }
        }
        return best
    }
}
