// LeetCode 1924 - Erect the Fence II
// https://leetcode.com/problems/erect-the-fence-ii/

class Solution {
    func outerTrees(_ trees: [[Int]]) -> [Double] {
        var pts = trees.map { (Double($0[0]), Double($0[1])) }
        // Fisher-Yates shuffle for Welzl-style incremental construction
        if pts.count > 1 {
            for i in stride(from: pts.count - 1, through: 1, by: -1) {
                let j = Int.random(in: 0...i)
                pts.swapAt(i, j)
            }
        }
        func dist(_ a: (Double, Double), _ b: (Double, Double)) -> Double {
            hypot(a.0 - b.0, a.1 - b.1)
        }
        func circle2(_ a: (Double, Double), _ b: (Double, Double)) -> ((Double, Double), Double) {
            let c = ((a.0 + b.0) / 2, (a.1 + b.1) / 2)
            return (c, dist(a, b) / 2)
        }
        func circle3(_ a: (Double, Double), _ b: (Double, Double), _ c: (Double, Double)) -> ((Double, Double), Double) {
            let ax = a.0, ay = a.1, bx = b.0, by = b.1, cx = c.0, cy = c.1
            let d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
            if abs(d) < 1e-12 {
                let cands = [circle2(a, b), circle2(a, c), circle2(b, c)]
                return cands.min(by: { $0.1 < $1.1 })!
            }
            let ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
            let uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
            let center = (ux, uy)
            return (center, dist(center, a))
        }
        func inside(_ cir: ((Double, Double), Double)?, _ p: (Double, Double)) -> Bool {
            guard let cir = cir else { return false }
            return dist(cir.0, p) <= cir.1 + 1e-9
        }
        var circle: ((Double, Double), Double)? = nil
        for i in 0..<pts.count {
            let p = pts[i]
            if circle == nil || !inside(circle, p) {
                circle = (p, 0.0)
                for j in 0..<i {
                    let q = pts[j]
                    if !inside(circle, q) {
                        circle = circle2(p, q)
                        for k in 0..<j {
                            let r = pts[k]
                            if !inside(circle, r) {
                                circle = circle3(p, q, r)
                            }
                        }
                    }
                }
            }
        }
        let (xy, r) = circle!
        return [xy.0, xy.1, r]
    }
}
