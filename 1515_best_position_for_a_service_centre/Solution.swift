// LeetCode 1515 - Best Position for a Service Centre
// https://leetcode.com/problems/best-position-for-a-service-centre/

class Solution {
    func getMinDistSum(_ positions: [[Int]]) -> Double {
        let n = Double(positions.count)
        var x = positions.reduce(0.0) { $0 + Double($1[0]) } / n
        var y = positions.reduce(0.0) { $0 + Double($1[1]) } / n
        func dist(_ a: Double, _ b: Double) -> Double {
            positions.reduce(0.0) { $0 + hypot(a - Double($1[0]), b - Double($1[1])) }
        }
        for _ in 0..<10000 {
            var nxNum = 0.0, nyNum = 0.0, den = 0.0
            var coincident: (Double, Double)? = nil
            for p in positions {
                let d = hypot(x - Double(p[0]), y - Double(p[1]))
                if d < 1e-12 {
                    coincident = (Double(p[0]), Double(p[1]))
                    break
                }
                nxNum += Double(p[0]) / d
                nyNum += Double(p[1]) / d
                den += 1 / d
            }
            let nx: Double
            let ny: Double
            if let c = coincident {
                nx = c.0; ny = c.1
            } else {
                nx = nxNum / den; ny = nyNum / den
            }
            if hypot(nx - x, ny - y) < 1e-8 {
                x = nx; y = ny
                break
            }
            x = nx; y = ny
        }
        return dist(x, y)
    }
}
