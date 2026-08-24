// LeetCode 3391 - Design a 3D Binary Matrix with Efficient Layer Tracking
// https://leetcode.com/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/

class Matrix3D {
    private var m: [[[Int]]]
    private var ones: [Int]
    private let n: Int

    init(_ n: Int) {
        self.n = n
        m = Array(repeating: Array(repeating: Array(repeating: 0, count: n), count: n), count: n)
        ones = Array(repeating: 0, count: n)
    }

    func setCell(_ x: Int, _ y: Int, _ z: Int) {
        if m[x][y][z] == 0 {
            m[x][y][z] = 1
            ones[x] += 1
        }
    }

    func unsetCell(_ x: Int, _ y: Int, _ z: Int) {
        if m[x][y][z] == 1 {
            m[x][y][z] = 0
            ones[x] -= 1
        }
    }

    func largestMatrix() -> Int {
        var best = -1, idx = 0
        for i in 0..<n {
            if ones[i] >= best {
                best = ones[i]
                idx = i
            }
        }
        return idx
    }
}
