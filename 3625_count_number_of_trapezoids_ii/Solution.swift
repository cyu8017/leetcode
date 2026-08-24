// LeetCode 3625 - Count Number of Trapezoids II
// https://leetcode.com/problems/count-number-of-trapezoids-ii/

class Solution {
    func countTrapezoids(_ points: [[Int]]) -> Int {
        let n = points.count
        var cnt1 = [String: [String: Int]]()
        var cnt2 = [Int: [String: Int]]()
        for i in 0..<n {
            let x1 = points[i][0], y1 = points[i][1]
            if i == 0 { continue }
            for j in 0..<i {
                let x2 = points[j][0], y2 = points[j][1]
                let dx = x2 - x1, dy = y2 - y1
                var k: Double, b: Double
                if dx == 0 {
                    k = 1e9
                    b = Double(x1)
                } else {
                    k = Double(dy) / Double(dx)
                    b = Double(y1 * dx - x1 * dy) / Double(dx)
                }
                let ks = String(k), bs = String(b)
                cnt1[ks, default: [:]][bs, default: 0] += 1
                let p = (x1 + x2 + 2000) * 4000 + (y1 + y2 + 2000)
                cnt2[p, default: [:]][ks, default: 0] += 1
            }
        }
        var ans = 0
        for e in cnt1.values {
            var s = 0
            for t in e.values {
                ans += s * t
                s += t
            }
        }
        for e in cnt2.values {
            var s = 0
            for t in e.values {
                ans -= s * t
                s += t
            }
        }
        return ans
    }
}
