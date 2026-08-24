// LeetCode 2013 - Detect Squares
// https://leetcode.com/problems/detect-squares/

class DetectSquares {
    private var cnt = [Int: Int]()

    init() {}

    private func key(_ x: Int, _ y: Int) -> Int {
        return (x << 32) ^ (y & 0xffffffff)
    }

    func add(_ point: [Int]) {
        cnt[key(point[0], point[1]), default: 0] += 1
    }

    func count(_ point: [Int]) -> Int {
        let x = point[0], y = point[1]
        var ans = 0
        for (k, c) in cnt {
            let px = k >> 32
            let py = Int(Int32(bitPattern: UInt32(k & 0xffffffff)))
            if px == x || py == y { continue }
            if abs(px - x) != abs(py - y) { continue }
            let c1 = cnt[key(px, y), default: 0]
            let c2 = cnt[key(x, py), default: 0]
            ans += c * c1 * c2
        }
        return ans
    }
}
