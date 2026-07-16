// LeetCode 0251 - Flatten 2D Vector
// https://leetcode.com/problems/flatten-2d-vector/

class Vector2D {
    private let vec: [[Int]]
    private var row = 0
    private var col = 0

    init(_ vec: [[Int]]) {
        self.vec = vec
        advance()
    }

    func next() -> Int {
        let value = vec[row][col]
        col += 1
        advance()
        return value
    }

    func hasNext() -> Bool {
        advance()
        return row < vec.count
    }

    private func advance() {
        while row < vec.count && col >= vec[row].count {
            row += 1
            col = 0
        }
    }
}
