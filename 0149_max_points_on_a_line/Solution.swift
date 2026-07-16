class Solution {
    func maxPoints(_ points: [[Int]]) -> Int {
        guard points.count > 2 else { return points.count }
        var best = 1

        for i in 0..<points.count {
            var slopes = [String: Int]()
            var localBest = 1
            for j in (i + 1)..<points.count {
                var dx = points[j][0] - points[i][0]
                var dy = points[j][1] - points[i][1]
                let divisor = gcd(dx, dy)
                dx /= divisor
                dy /= divisor
                if dx < 0 || (dx == 0 && dy < 0) {
                    dx = -dx
                    dy = -dy
                }
                let slope = "\(dx),\(dy)"
                slopes[slope, default: 0] += 1
                localBest = max(localBest, slopes[slope]! + 1)
            }
            best = max(best, localBest)
        }
        return best
    }

    private func gcd(_ a: Int, _ b: Int) -> Int {
        var a = abs(a)
        var b = abs(b)
        while b != 0 {
            let remainder = a % b
            a = b
            b = remainder
        }
        return a
    }
}