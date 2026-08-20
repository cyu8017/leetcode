// LeetCode 1453 - Maximum Number of Darts Inside of a Circular Dartboard
// https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/

class Solution {
    func numPoints(_ darts: [[Int]], _ r: Int) -> Int {
        var ans = darts.isEmpty ? 0 : 1
        let rr = Double(r)
        for i in 0..<darts.count {
            let x1 = Double(darts[i][0]), y1 = Double(darts[i][1])
            for j in (i + 1)..<darts.count {
                let x2 = Double(darts[j][0]), y2 = Double(darts[j][1])
                let dx = x2 - x1, dy = y2 - y1
                let d2 = dx * dx + dy * dy
                if d2 > 4 * rr * rr || d2 == 0 { continue }
                let d = d2.squareRoot()
                let h = (rr * rr - d2 / 4).squareRoot()
                let mx = (x1 + x2) / 2, my = (y1 + y2) / 2
                for sign in [-1.0, 1.0] {
                    let cx = mx + sign * (-dy) * h / d
                    let cy = my + sign * dx * h / d
                    let count = darts.filter {
                        let x = Double($0[0]), y = Double($0[1])
                        return (x - cx) * (x - cx) + (y - cy) * (y - cy) <= rr * rr + 1e-7
                    }.count
                    ans = max(ans, count)
                }
            }
        }
        return ans
    }
}
