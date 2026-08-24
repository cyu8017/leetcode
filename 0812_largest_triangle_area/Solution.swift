// LeetCode 0812 - Largest Triangle Area
// https://leetcode.com/problems/largest-triangle-area/

class Solution {
    func largestTriangleArea(_ points: [[Int]]) -> Double {
        var best = 0.0
        let n = points.count
        for i in 0..<n {
            let x1 = points[i][0], y1 = points[i][1]
            for j in (i + 1)..<n {
                let x2 = points[j][0], y2 = points[j][1]
                for k in (j + 1)..<n {
                    let x3 = points[k][0], y3 = points[k][1]
                    let area = abs(Double(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))) / 2.0
                    best = max(best, area)
                }
            }
        }
        return best
    }
}
