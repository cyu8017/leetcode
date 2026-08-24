// LeetCode 0963 - Minimum Area Rectangle II
// https://leetcode.com/problems/minimum-area-rectangle-ii/

class Solution {
    func minAreaFreeRect(_ points: [[Int]]) -> Double {
        let n = points.count
        var groups = [String: [(Int, Int)]]()
        for i in 0..<n {
            for j in (i + 1)..<n {
                let cx = points[i][0] + points[j][0]
                let cy = points[i][1] + points[j][1]
                let dx = points[i][0] - points[j][0]
                let dy = points[i][1] - points[j][1]
                let dist = dx * dx + dy * dy
                let key = "\(cx)#\(cy)#\(dist)"
                groups[key, default: []].append((i, j))
            }
        }
        var ans = Double.greatestFiniteMagnitude
        for pairs in groups.values {
            for a in 0..<pairs.count {
                for b in (a + 1)..<pairs.count {
                    let p1 = pairs[a].0, p2 = pairs[b].0, q2 = pairs[b].1
                    let d1 = hypot(Double(points[p1][0] - points[p2][0]), Double(points[p1][1] - points[p2][1]))
                    let d2 = hypot(Double(points[p1][0] - points[q2][0]), Double(points[p1][1] - points[q2][1]))
                    let area = d1 * d2
                    if area > 0 { ans = min(ans, area) }
                }
            }
        }
        return ans == Double.greatestFiniteMagnitude ? 0.0 : ans
    }
}
